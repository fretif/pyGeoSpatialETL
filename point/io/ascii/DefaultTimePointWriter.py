#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# CoverageProcessing is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# CoverageProcessing is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# Author : Fabien Rétif - fabien.retif@zoho.com
#
from __future__ import division, print_function, absolute_import
from point.io.MultiPointWriter import MultiPointWriter
from point.TimeMultiPoint import TimeMultiPoint
from utils.VariableUnits import VariableUnits
from netCDF4 import Dataset
from netCDF4 import date2num
from numpy import float32
from numpy import float64
import numpy as np
import logging
import pandas


class DefaultTimePointWriter(MultiPointWriter):

    def __init__(self, s,index_point,myFile):
        MultiPointWriter.__init__(self, s, myFile);

        if not isinstance(self.points, TimeMultiPoint):
            raise ValueError("This writer supports only TimeMultiPoint object")

        self.index_x = index_point

        index = pandas.DatetimeIndex(self.points.read_axis_t())
        self.data = pandas.DataFrame(index=index)

    def close(self):
        self.data.to_csv(self.filename, sep='\t', columns=list(self.data), header=False, encoding='utf-8', na_rep="NaN")

        file = open(self.filename, "r+")
        old = file.read()  # read everything in the file
        file.seek(0)  # rewind

        file.write("############################################################ \n\
# Station : " + str(self.points.name_station) + " \n\
# Coordinate Reference System : WGS84 \n\
# Longitude : " + str(self.points.x_coord) + " \n\
# Latitude : " + str(self.points.y_coord) + " \n\
# Data source : " + str(self.points.data_source) + " \n\
# Meta Data : " + str(self.points.meta_data) + " \n\
# Time zone : UTC \n\
# Separator: Tabulation \\t \n\
# Column 1: year-month-day hour:minute:second UTC \n")

        column = 2
        for key in list(self.data):
            file.write("# Column " + str(column) + ": " + str(key) + " " + str(
                VariableUnits.CANONICAL_UNITS[key]) + " FillValue: NaN \n")
            column = column + 1

        file.write("# Generated with pyGeoSpatialETL\n")
        file.write("############################################################\n")

        file.write(old)  # write the new line before
        file.close()

    def write_variable_sea_surface_height(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Surface Height\'')

        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_surface_height_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_surface_height'] = data

    def write_variable_sea_surface_temperature(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Surface Temperature\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_surface_temperature_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_surface_temperature'] = data

    def write_variable_longitude(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Longitude\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_longitude_at_time(time)[self.index_x]
            time_index += 1

        self.data['longitude'] = data

    def write_variable_latitude(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Latitude\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_latitude_at_time(time)[self.index_x]
            time_index += 1

        self.data['latitude'] = data

    def write_variable_sea_surface_wave_significant_height(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Surface Wave Significant Height\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_surface_wave_significant_height_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_surface_wave_significant_height'] = data

    def write_variable_sea_surface_wave_mean_period(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Surface Wave Mean Period\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_surface_wave_mean_period_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_surface_wave_mean_periode'] = data

    def write_variable_sea_surface_salinity(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Surface Salinity\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_surface_salinity_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_surface_salinity'] = data

    def write_variable_sea_surface_density(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Surface Density\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_surface_density_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_surface_density'] = data

    def write_variable_sea_water_turbidity(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Water Turbidity\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_water_turbidity_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_water_turbidity'] = data

    def write_variable_bathymetry(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Bathymetry\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_bathymetry_at_time(time)[self.index_x]
            time_index += 1

        self.data['bathymetry'] = data

    def write_variable_wind_speed_10m(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Wind Speed 10m\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_wind_speed_10m_at_time(time)[self.index_x]
            time_index += 1

        self.data['wind_speed_10m'] = data

    def write_variable_wind_from_direction_10m(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Wind From Direction 10m\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_wind_from_direction_10m_at_time(time)[self.index_x]
            time_index += 1

        self.data['wind_from_direction_10m'] = data

    def write_variable_wind_to_direction_10m(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Wind To Direction 10m\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_wind_to_direction_10m_at_time(time)[self.index_x]
            time_index += 1

        self.data['wind_from_direction_10m'] = data

    def write_variable_surface_air_pressure(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Surface Air Pressure\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_surface_air_pressure_at_time(time)[self.index_x]
            time_index += 1
        self.data['surface_air_pressure'] = data

    def write_variable_rainfall_amount(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Rainfall Amount\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_rainfall_amount_at_time(time)[self.index_x]
            time_index += 1
        self.data['rainfall_amount'] = data

    def write_variable_sea_water_pressure_at_sea_water_surface(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Water Pressure At Sea Water Surface\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_water_pressure_at_sea_water_surface_at_time(time)[self.index_x]
            time_index += 1

        self.data['sea_water_pressure_at_sea_water_surface'] = data

    def write_variable_sea_water_electrical_conductivity(self):
        logging.info('[DefaultTimePointWriter] Writing variable \'Sea Water Electrical Conductivity\'')
        data = np.zeros([self.points.get_t_size()])
        data[:] = np.nan
        time_index = 0
        for time in self.points.read_axis_t():
            data[time_index] = self.points.read_variable_sea_water_electrical_conductivity_at_time(time)[
                self.index_x]
            time_index += 1

        self.data['sea_water_electrical_conductivity'] = data