import React, { Component } from 'react';
import { connect } from 'react-redux';

import Chart from '../components/chart';
import GoogleMap from '../components/google_map';

class WeatherList extends Component {
    renderWeather(cityData) {
        const name = cityData.city.name;
        const temps = cityData.list.map(weather => weather.main.temp);
        const pressures = cityData.list.map(weather => weather.main.pressure);
        const humidities = cityData.list.map(weather => weather.main.humidity);
        const { lon, lat } = cityData.city.coord;
        
        return (
            <tr key={name}>
                <td className="city-column">
                    <GoogleMap lon={lon} lat={lat}/>
                </td>
                <td className="column">
                    <Chart data={temps} color="orange" units="K"/>
                </td>
                <td className="column">
                    <Chart data={pressures} color="green" units="hPa"/>
                </td>
                <td className="column">
                    <Chart data={humidities} color="black" units="%"/>
                </td>
            </tr>
        )
    }
    
    render() {
        return (
            <table className="table table-hover">
                <thead>
                    <tr>
                        <th className="city-column">City</th>
                        <th className="column">Temperature (K)</th>
                        <th className="column">Pressure    (hPa)</th>
                        <th className="column">Humidity    (%)</th>
                    </tr>
                </thead>
                <tbody>
                    {this.props.weather.map(this.renderWeather)}
                </tbody>
            </table>
        )
    }
}

function mapStateToProps({weather}) {
    return { weather }; // same as { weather: weather }
}

export default connect(mapStateToProps)(WeatherList);