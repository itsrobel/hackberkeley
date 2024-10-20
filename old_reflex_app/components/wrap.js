import React, { useEffect, useRef } from 'react';

const HtmlWrapper = () => {
  const containerRef = useRef(null);

  useEffect(() => {
    const fetchHtml = async () => {
      const response = await fetch('/path/to/your/simple-html.html');
      const html = await response.text();
      if (containerRef.current) {
        containerRef.current.innerHTML = html;
      }
    };

    fetchHtml();
  }, []);

  return <div ref={containerRef}></div>;
};

export default HtmlWrapper;