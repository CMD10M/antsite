import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {Line} from '@ant-design/charts';
import React, { useState, useEffect } from "react";

const App = () => {

  const DemoLine = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios.get("http://127.0.0.1:8000/integer-pairs/");
      setData(result.data);
    };

    fetchData();
  }, []);

  const config = {
    data,
    padding: 'auto',
    xField: 'hour',
    yField: 'load',
    xAxis: {
      // type: 'timeCat',
      tickCount: 5,
    },
  };

  return <Line {...config} />;
};



  return (
    <ul>
      <div style={{textAlign: 'center'}}>
      <h2> Basic Line Graph</h2>
  <DemoLine/>
  </div>
    </ul>

  );
  };

export default App;
