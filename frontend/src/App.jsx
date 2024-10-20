"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
require("./App.css");
const map_1 = __importDefault(require("./components/map"));
const react_1 = __importDefault(require("react"));
function App() {
    return (<div className="App">
      <map_1.default />
      {/* <header className="App-header"> */}
      {/*   <img src={logo} className="App-logo" alt="logo" /> */}
      {/*   <p> */}
      {/*     Edit <code>src/App.js</code> and save to reload. */}
      {/*   </p> */}
      {/*   <a */}
      {/*     className="App-link" */}
      {/*     href="https://reactjs.org" */}
      {/*     target="_blank" */}
      {/*     rel="noopener noreferrer" */}
      {/*   > */}
      {/*     Learn React */}
      {/*   </a> */}
      {/* </header> */}
    </div>);
}
exports.default = App;
