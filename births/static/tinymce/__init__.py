from fanstatic import Library, Resource

library = Library('tinymce', 'resources')

tinymce = Resource(library, 'tiny_mce_src.js', minified='tiny_mce.js')

tinymcepopup = Resource(library, 'tiny_mce_popup.js')
