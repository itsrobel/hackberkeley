import React, { useState, useEffect, useRef } from "react";
import maphtml from "./time_heatmap.html?raw";
import $ from "jquery";

interface JQueryHtmlLoaderProps {
  filePath: string;
}

const JQueryHtmlLoader: React.FC<JQueryHtmlLoaderProps> = ({ filePath }) => {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const loadHtmlFile = () => {
      if (containerRef.current) {
        $(containerRef.current).load(
          filePath,
          (response: any, status: any, xhr: any) => {
            if (status === "error") {
              console.error(
                `Error loading HTML file: ${xhr.status} ${xhr.statusText}`,
              );
              $(containerRef.current).html("<p>Error loading HTML content</p>");
            }
          },
        );
      }
    };

    loadHtmlFile();
  }, [filePath]);

  return <div ref={containerRef}></div>;
};

// export default JQueryHtmlLoader;

function MapLoader() {
  // const [htmlContent, setHtmlContent] = useState<string>("");

  // useEffect(() => {
  //   fetch("./time_heatmap.html")
  //     .then((response: any) => response.text())
  //     .then((thisHtml: string) => {
  //       setHtmlContent(thisHtml);
  //
  //       console.log(thisHtml);
  //       console.log("t");
  //     });
  // }, [htmlContent]);
  console.log(maphtml);
  // return <div>{md.documentElement}</div>;
  // return <Container child={md.documentElement}></Container>;
  // return <iframe src={perf}></iframe>; /* like this */

  // let de = md.
  // return md;
  return <div dangerouslySetInnerHTML={{ __html: maphtml }} />;
}

function Map() {
  return (
    <div>
      {/* <maphtml/> */}
      <JQueryHtmlLoader filePath="./time_heatmap.html" />

      {/* <MapLoader /> */}
    </div>
  );
}
export default Map;
