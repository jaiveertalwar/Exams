

"use strict";

function navbar_scrollto(node) {
    var sidebar = $('#sidebar-wrapper').first()[0];
    var navbar = $(sidebar).find('div.sidebar').first()[0];

    if (sidebar && navbar) {
        var do_scroll = false;
        if ($(navbar).is(':visible')) {
            if ($.scrollTo) {
                do_scroll = true;
            } else {
                console.log('$.scrollTo not found');
            }
        }
        if (do_scroll) {
            // console.log("scrollTo", node);
            if (!($(node).isOnScreen())) {
                $(sidebar).scrollTo($(node), {
                    axis: 'y',
                    offset: { top: -100 }
                });
            }
        }
    } else {
        console.log('sidebar is', sidebar);
        console.log('navbar is', navbar);
    }
}
function navbar_update(nodeurl) {
    var content = $('#content-wrapper');
    var navbar = $('#sidebar-wrapper').find('div.sidebar').first()[0];
    ($(content)
        .find('a.headerlink.youarehere')
        .removeClass('youarehere')
        .text('¶')
    );
    ($('#navbar-top')
        .find('a.reference.internal')
        .removeClass('youarehere')
    );
    $(navbar).find('a.youarehere').removeClass('youarehere');
    if (nodeurl) {
        ($(content)
            .find('a.headerlink[href="' + nodeurl + '"]')
            .addClass('youarehere')
            .text('⬅')
        );

        ($('#navbar-top')
            .find('a.reference.internal[href="' + nodeurl + '"]')
            .addClass('youarehere')
        );

        var navbarlink = $(navbar).find('a[href="' + nodeurl + '"]');

        if (navbarlink) {
            navbarlink.addClass('youarehere');
            navbar_scrollto(navbarlink); // # navbar a.youarehere
        } else {
            console.log("nodeurl not found");
            console.log(nodeurl);
        }
    } else {
        console.log("nodeurl is false");
        console.log(nodeurl);
    }
}

function navbar__remap_sphinx_toc_links() {
    var content = $('#content-wrapper');
    ($(content)
        .find('a.headerlink')
        .map(function(node) {
            console.log(node);
            $(node.previousSibling).attr('href', $(node).attr('href'));
        })
    );
}

function navbar__add_top_button() {
    ($('<button type="button" class="toplink navbar-toggle"><span><a href="#">Top</a></span></button>')
     .appendTo('body'));
}

function navbar_init() {
    // require('jquery.scrollto')
    //var scriptstr = '<script src="https://cdn.jsdelivr.net/jquery.scrollto/2.1.0/jquery.scrollTo.min.js"></script>';
    //$(scriptstr).appendTo("head");
    navbar_update(window.location.hash);

    navbar__remap_sphinx_toc_links();
    navbar__add_top_button();

    window.onhashchange = function(e) {
        // console.log(e); // e.newURL , e.oldURL
        var loc_hash_url = window.location.hash;
        console.log(loc_hash_url);
        if (loc_hash_url != false) {
            navbar_update(loc_hash_url);
        };
    };
}


$(document).ready(navbar_init);