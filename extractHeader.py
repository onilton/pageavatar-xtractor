#!/usr/bin/python
# -*- coding: utf-8 -*-

from ghost import Ghost
import re
from sys import argv


#rawDomainName = "http://corta-fitas.blogs.sapo.pt/"
if len(argv)>1:
    rawDomainName = argv[1]
else:
    rawDomainName = "http://emtempo.com.br/"

ghost = Ghost(wait_timeout=60, viewport_size=(1600, 900))
page, extra_resources = ghost.open(rawDomainName)



#page, extra_resources = ghost.open("http://www.emtempo.com.br/")
# ghost.capture_to('header.png', selector="header")
# ghost.capture_to('header.png', selector="header div.aet-shapes img")

# var target = $('#target').show();
#target = target.add(target.parentsUntil('body')).siblings().hide();

#result, resources = ghost.evaluate(
#    "$(document).ready(function() { var target = $('#apDiv2').show(); target = target.add(target.parentsUntil('body')).siblings().hide(); }); ")


#page, resources = ghost.wait_for_page_loaded()

# $('#target').show().parentsUntil('body').andSelf().siblings().hide();


domainName = re.sub(r'/$', r'', rawDomainName)
domainName = re.sub(r'^(https?://)www.', r'\1', domainName)


imageName = re.sub(r'^(https?://)', r'', domainName)
imageName = re.sub(r'\W', r'_', imageName)



domainNameWithWWW = re.sub(r'^(https?://)(.*)', r'\1www.\2', domainName)
possibleDomainLinks = ['/', '//', domainName+'/', domainName, domainNameWithWWW]

anchorSelectorsList = [ """a[href="%s"]""" % selector for selector in possibleDomainLinks ] #'a[href="ABC"], '

selectorsString =  ', '.join(anchorSelectorsList)

print "selectorsString=", selectorsString

result, resources = ghost.evaluate("""
// Jquery safe load from http://css-tricks.com/snippets/jquery/load-jquery-only-if-not-present/
var jQueryScriptOutputted = false;
function initJQuery() {
    
    //if the jQuery object isn't available
    if (typeof(jQuery) == 'undefined') {
    
        if (! jQueryScriptOutputted) {
            //only output the script once..
            jQueryScriptOutputted = true;

            var scriptBlock = document.createElement('script');
            scriptBlock.type = "text/javascript";
            scriptBlock.src = "http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js";

            ( document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0] ).appendChild( scriptBlock );
            
            // OLD WAY output the script (load it from google api)
            //document.write('<scr' + 'ipt type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></scr' + 'ipt>');
        }
        setTimeout("initJQuery()", 50);
    } else {
                        
        jQuery.noConflict();
        jQuery(function($) {  

            // do anything that needs to be done on document.ready
            // don't really need this dom ready thing if used in footer

            $(document).ready(function() {
                'use strict';
                var logoBlock =  $('"""+ selectorsString +"""').closest(':not(:only-child)').sort(function (a, b) {
                     return $(a).width() <= $(b).width() ? 1 : -1;   // <= Is important because if width is the same, keep the first as first
                }).first() ;
                //var logoBlock
                //var logoBlock =  $('#apDiv2') ;
                //var logoBlock =  $('.first > .logo') ;
                //var logoBlock =  $('.bloco-logo') ;
                //var logoBlock =  $('h1#logo1') ;
                //var logoBlock =  $('#header > h1 > a') ;
                //var logoBlock =  $('div#logo') ;
                //var logoBlock =  $('header#masthead > a') ;
                //var logoBlock =  $('#logo') ;

                logoBlock.show().parentsUntil('body').andSelf().siblings().hide();
                /* one item */
                / *li:first-child:nth-last-child(1) { */

                var closestWithSiblings = logoBlock.closest(':not(:only-child)').css('margin-top', '200px').css('margin-bottom','200px');
                //logoBlock.show().parentsUntil('body',':only-child').andSelf().css('margin-top', '200px').css('margin-bottom','200px');
                //logoBlock.show().parentsUntil('body',':not(:only-child)').css('height', '600px');
                closestWithSiblings.parentsUntil('body').css('height', '600px');
                //closestWithSiblings.parentsUntil('body').css('height', '600px').append(closestWithSiblings);
                

                //$('#apDiv2').css('margin-top', '200px').css('margin-bottom','200px');
                $('body').append('<div style="height:1000px;"></div>');
                $("html, body").css("overflow", "hidden"); //jquery trick to hide scrollbar
                function unloadScrollBars() {
                    document.documentElement.style.overflow = 'hidden';
                    document.documentElement.scroll = "no";
                    document.body.style.overflow = 'hidden';
                    document.body.scroll = "no";
                }
                unloadScrollBars();
                alert("done");
            });


        });
    }
            
}
initJQuery();
    
""")

result, resources = ghost.wait_for_alert()


#jQuery(function($) {
#    'use strict';
#    $('#apDiv2').show().parentsUntil('body').andSelf().siblings().hide();
#    /* one item */
#/ *li:first-child:nth-last-child(1) { */
#    $('#apDiv2').show().parentsUntil('body',':only-child').andSelf().css('margin-top', '200px').css('margin-bottom','200px');
#    $('#apDiv2').show().parentsUntil('body',':not(:only-child)').css('height', '600px');
#;
#
#    //$('#apDiv2').css('margin-top', '200px').css('margin-bottom','200px');
#    $('body').append('<div style="height:1000px;"></div>');
#});

#jQuery(function($) {
#    'use strict';
#    //var logoBlock
#    //var logoBlock =  $('#apDiv2') ;
#    //var logoBlock =  $('.first > .logo') ;
#    //var logoBlock =  $('.bloco-logo') ;
#    var logoBlock =  $('h1#logo1') ;
#    //var logoBlock =  $('a.inicio') ;
#    //var logoBlock =  $('div#logo') ;
#    //var logoBlock =  $('header#masthead > a') ;
#    //var logoBlock =  $('#logo') ;
#    logoBlock.show().parentsUntil('body').andSelf().siblings().hide();
#    /* one item */
#/ *li:first-child:nth-last-child(1) { */
#
#    var closestWithSiblings = logoBlock.closest(':not(:only-child)').css('margin-top', '200px').css('margin-bottom','200px');
#    //logoBlock.show().parentsUntil('body',':only-child').andSelf().css('margin-top', '200px').css('margin-bottom','200px');
#    //logoBlock.show().parentsUntil('body',':not(:only-child)').css('height', '600px');
#    closestWithSiblings.parentsUntil('body').css('height', '600px');
#    //closestWithSiblings.parentsUntil('body').css('height', '600px').append(closestWithSiblings);
#    
#;
#
#    //$('#apDiv2').css('margin-top', '200px').css('margin-bottom','200px');
#    $('body').append('<div style="height:1000px;"></div>');
#});

#//take the image and do everything with background color and images with repeat 


    #$('#apDiv2').show().parentsUntil('body').andSelf().siblings().hide();

#jQuery(function($) {
#    'use strict';
#    $('#jq-siteLogo').show().parentsUntil('body').andSelf().siblings().hide();
#    $('body').append('<div style="height:1000px;"></div>');
#});
#
#
#
#jQuery(function($) {
#    'use strict';
#    $('.bloco-logo').show().parentsUntil('body').andSelf().siblings().remove();
#    $('body').append('<div style="height:1000px;"></div>');
#});
#
#jQuery(function($) {
#    'use strict';
#    $('.first > .logo').show().parentsUntil('body').andSelf().siblings().remove();
#});



    #$('#apDiv2').show().parentsUntil('body').andSelf().siblings().css('visibility', 'hidden');

#result, resources = ghost.evaluate(
#    "$(document).ready(function() { $('nav.aet-nav').hide(); }); ")


#result, resources = ghost.evaluate(
#    "$(document).ready(function() { $('div.aet-header').hide(); }); ")


#result, resources = ghost.evaluate("document.getElementById('apDiv2').style.display = 'none';")


#result, resources = ghost.evaluate(
#    "$(document).ready(function() { var target = $('#apDiv2').show(); target = target.add(target.parentsUntil('body')).siblings().hide(); }); ")

#ghost.evaluate("window.document.getElementById('apDiv2').style.visibility = 'hidden'; ")
#ghost.evaluate("window.document.getElementById('apDiv2').style.visibility = 'hidden'; ")
#ghost.evaluate("$('div:not(#myDiv)').show();")
#ghost.evaluate("v$('div:not(#myDiv)').show();")


#### ghost.evaluate("window.scroll(0, 2000);")



#result, resources = ghost.evaluate(
#    "alert('Okk');")

#result, resources = ghost.wait_for_alert()

#$(document).ready(function() {
#      alert("document ready occurred!");
#});

ghost.capture_to(imageName+'.png')
#ghost.capture_to('header.png')
# assert page.http_status==200 and 'jeanphix' in ghost.content
