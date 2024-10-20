# """Welcome to Reflex! This file outlines the steps to create a basic app."""

# import reflex as rx

# from rxconfig import config


# class State(rx.State):
#     """The app state."""

#     ...


# test = '''
# <head>
    
#     <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
#         <script>
#             L_NO_TOUCH = false;
#             L_DISABLE_3D = false;
#         </script>
    
#     <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
#     <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
#     <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
#     <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
#     <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
#             <meta name="viewport" content="width=device-width,
#                 initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
#             <style>
#                 #map_e0e3de0bf7df8a8bfd66cb5e03298ef7 {
#                     position: relative;
#                     width: 100.0%;
#                     height: 100.0%;
#                     left: 0.0%;
#                     top: 0.0%;
#                 }
#                 .leaflet-container { font-size: 1rem; }
#             </style>
        
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-groupedlayercontrol/0.6.1/leaflet.groupedlayercontrol.min.js"></script>
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet-groupedlayercontrol/0.6.1/leaflet.groupedlayercontrol.min.css"/>
# </head>
# <body>
    
    
#             <div class="folium-map" id="map_e0e3de0bf7df8a8bfd66cb5e03298ef7" ></div>
        
# </body>
# <script>
    
    
#             var map_e0e3de0bf7df8a8bfd66cb5e03298ef7 = L.map(
#                 "map_e0e3de0bf7df8a8bfd66cb5e03298ef7",
#                 {
#                     center: [36.62, 2.3],
#                     crs: L.CRS.EPSG3857,
#                     zoom: 12,
#                     zoomControl: true,
#                     preferCanvas: false,
#                 }
#             );
#             L.control.scale().addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);

            

        
    
#             var tile_layer_04e6b6569dd942765962b220f22beda4 = L.tileLayer(
#                 "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
#                 {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors \u0026copy; \u003ca href=\"https://carto.com/attributions\"\u003eCARTO\u003c/a\u003e", "detectRetina": false, "maxNativeZoom": 20, "maxZoom": 20, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abcd", "tms": false}
#             );
        
    
#             tile_layer_04e6b6569dd942765962b220f22beda4.addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);
        
    
#             var tile_layer_401171a4c12d5a6f53ad0aa2d988d4c2 = L.tileLayer(
#                 "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
#                 {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 19, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
#             );
        
    
#             tile_layer_401171a4c12d5a6f53ad0aa2d988d4c2.addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);
        
    
#             var feature_group_d279203d25a41ba2d53ea9e766ea9887 = L.featureGroup(
#                 {}
#             );
        
    
#             var marker_c1725b8755315fd37031f81749f0357d = L.marker(
#                 [36.63, 2.26],
#                 {}
#             ).addTo(feature_group_d279203d25a41ba2d53ea9e766ea9887);
        
    
#             marker_c1725b8755315fd37031f81749f0357d.bindTooltip(
#                 `<div>
#                      <h4>Blue Marker.</h4>
#                  </div>`,
#                 {"sticky": true}
#             );
        
    
#             feature_group_d279203d25a41ba2d53ea9e766ea9887.addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);
        
    
#             var tile_layer_39220c8a2d5c7f9eda02eb89fb087f8c = L.tileLayer(
#                 "https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/6fe81f97c79a295d9337770b17fbd30e-badae8cb8a4871c642f09f10d8368ad3/tiles/{z}/{x}/{y}",
#                 {"attribution": "Map Data \u0026copy; \u003ca href=\"https://earthengine.google.com/\"\u003eGoogle Earth Engine\u003c/a\u003e", "detectRetina": false, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
#             );
        
    
#             tile_layer_39220c8a2d5c7f9eda02eb89fb087f8c.addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);
        
    
#             var tile_layer_0dd273a920f074556abcd4554b15f3fa = L.tileLayer(
#                 "https://earthengine.googleapis.com/v1/projects/earthengine-legacy/maps/cc2275c21cea729c8c08922342e9e83f-ccd9fe81dd019a73d7ae96ffdc7a3f98/tiles/{z}/{x}/{y}",
#                 {"attribution": "Map Data \u0026copy; \u003ca href=\"https://earthengine.google.com/\"\u003eGoogle Earth Engine\u003c/a\u003e", "detectRetina": false, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
#             );
        
    
#             tile_layer_0dd273a920f074556abcd4554b15f3fa.addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);
        
    
#             var layer_control_ef0c3a3365c3f2f6f989f13d29a88dc2_layers = {
#                 base_layers : {
#                     "Dark Matter" : tile_layer_04e6b6569dd942765962b220f22beda4,
#                     "Open Street Map" : tile_layer_401171a4c12d5a6f53ad0aa2d988d4c2,
#                 },
#                 overlays :  {
#                 },
#             };
#             let layer_control_ef0c3a3365c3f2f6f989f13d29a88dc2 = L.control.layers(
#                 layer_control_ef0c3a3365c3f2f6f989f13d29a88dc2_layers.base_layers,
#                 layer_control_ef0c3a3365c3f2f6f989f13d29a88dc2_layers.overlays,
#                 {"autoZIndex": true, "collapsed": false, "position": "topright"}
#             ).addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);

        
    

#             L.control.groupedLayers(
#                 null,
#                 {
#                     "--------MARKERS LAYER--------" : {
#                         "Blue Marker" : feature_group_d279203d25a41ba2d53ea9e766ea9887,
#                     },
#                     "--GOOLE EARTH ENGINE LAYERS--" : {
#                         "Image Satellite 1" : tile_layer_39220c8a2d5c7f9eda02eb89fb087f8c,
#                         "Image Satellite 2" : tile_layer_0dd273a920f074556abcd4554b15f3fa,
#                     },
#                 },
#                 {"collapsed": false},
#             ).addTo(map_e0e3de0bf7df8a8bfd66cb5e03298ef7);
# </script>
# '''

# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
        
#         rx.vstack(
#     rx.html(test),
# ),
#         rx.logo(),
#     )


# app = rx.App()
# app.add_page(index)


import reflex as rx
# from wrap import html_wrapper
from .components import wrap
def index():
    return rx.box(
        rx.heading("Welcome to my Reflex app!"),
        wrap.HtmlWrapper()
    )

app = rx.App()
app.add_page(index)