import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import DataProvider from './DataProvider';
import PDFViewer from './pdfviewer/pdfviewer';
import PDFJSBackend from './backend/pdfjs';
import Table from './Table';
import axios from 'axios';
import './App.css';

/*
const App = () => (
  <div>
    <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
  </div>
);
*/


/*
const dataTable = (
  <div>
    <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
    <button className="btn btn-default">Testing Button</button>
  </div>
);
*/
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      selectedFile: null
    };

    
  }

  onChangeHandler = event => {
    console.log(`File being added: ${event.target.files[0].name}`);
    this.setState({
      selectedFile: URL.createObjectURL(event.target.files[0]),
      loaded: 0,
    });
  };

  clickButton = event => {
    console.log("Sending file to be processed...");
    const data = new FormData();
    data.append('file', this.state.selectedFile);

    try {
      axios.post("http://localhost:8000/upload", data, {

      }).then(res =>  {
        console.log(res.statusText)
        console.log(res.data)
      });
    }
    catch (error) {
      console.log(error);
    }
  };

  render() {
    let transcriptImage
    if (this.state.selectedFile != null){
      // transcriptImage = <img src={this.state.selectedFile} />
      transcriptImage = <object width="100%" height="400" data={this.state.selectedFile} type="application/pdf"></object>
    }
    else {
      transcriptImage = <div className="transimg">No Transcript Loaded</div>
    }
    return (
      <div id='root'>
        <div>
          <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
        </div>
        <div className="topnav">
            <a href="#">BC Programs</a>
            <a href="#">BC Classes</a>
            <a href="#">Audit Program</a>
            <a href="#">My Profile</a>
        </div>
        <div className="header">
            <h1>BC Advisor</h1>
            <p>Your Bellevue College Online Advisor</p>
        </div>
        <div className="row">
          <div className="leftcolumn">
            <div className="card">
              <h2>Transcript Uploader</h2>
              <h5>Upload your transcript</h5>
              <p> Upload a PDF file of your transcript:<br />
                <input type="file" name="datasize" size="30" onChange={this.onChangeHandler} />
              </p>
                <div>
                  <input type="submit" value="Submit" onClick={this.clickButton} />
                </div>
            </div>      
          </div>
          <div className="rightcolumn">
            <div className="card">
              <h2>Your Transcript</h2>
              <div className="transimg">
                {transcriptImage}
              </div>
              <p></p>
            </div>      
          </div>
        </div>
        <div className="PDFViewer">
          <PDFViewer 
            backend={PDFJSBackend}
            src='/myPDF.pdf'/>
        </div>
        <div className="footer">
            <h2>BC Advisor</h2>
        </div>
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById("app")
);


/*
<div>
  <div>
    <DataProvider endpoint="api/users/" render={data => <Table data={data} />} />
  </div>
  <div className="container">
    <div className="row">
      <div className="col-md-6">
        <form method="post" action="#" id="#">
          <div className="form-group files">
            <label>Upload Your Transcript </label>
            <input type="file" className="form-control" multiple="" name="file" onChange={this.onChangeHandler} />
          </div>
        </form>
      </div>
      </div>
  </div>
  <div className="row">
    <div className="col-md-6">
        <div>
          <button type="button" onClick={this.clickButton}>Submit</button>
        </div>
      </div>
    </div>
</div>
*/