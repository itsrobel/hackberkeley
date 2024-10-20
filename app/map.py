import reflex as rx


class MapContainer(rx.NoSSRComponent):
    library = "react-leaflet"

    tag = "MapContainer"

    center: rx.Var[list]

    zoom: rx.Var[int]

    scroll_wheel_zoom: rx.Var[bool]

    # Can also pass a url like: https://unpkg.com/leaflet/dist/leaflet.css
    def add_imports(self):
        return {"": ["leaflet/dist/leaflet.css"]}


class TileLayer(rx.NoSSRComponent):
    library = "react-leaflet"

    tag = "TileLayer"

    url: rx.Var[str]


map_container = MapContainer.create
tile_layer = TileLayer.create
