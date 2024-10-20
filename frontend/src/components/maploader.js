import React, { useState, useEffect } from "react";

function MapLoader() {
  const [mapContent, setMapContent] = useState("");

  useEffect(() => {
    fetch("./map.html")
      .then((response) => response.text())
      .then((html) => {
        setMapContent(html);
        console.log(html);
      });
  }, []);
  return <div dangerouslySetInnerHTML={{ __html: mapContent }} />;
}

function Map() {
  return (
    <div>
      <MapLoader />
    </div>
  );
}
export default Map;
