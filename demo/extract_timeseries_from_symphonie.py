#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# pySpatialETL is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# pySpatialETL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

# Lien vers le dossier de la lib
import sys
sys.path = ['../'] + sys.path

from spatialetl.point.TimeLevelMultiPoint import TimeLevelMultiPoint
from spatialetl.point.TimeMultiPoint import TimeMultiPoint
from spatialetl.point.io.netcdf.symphonie.SYMPHONIEReader import SYMPHONIEReader
from spatialetl.point.io.netcdf.DefaultWriter import DefaultWriter as NcWriter

import logging
from datetime import timedelta

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

    points = {}
    points['Point_1'] = [-68.4544444444444, 51.6213888888889]
    points['Point_2'] = [-68.3194444444444, 51.5152777777778]
    points['Point_3'] = [-68.3061111111111, 51.3888888888889]
    stationCoords = [points['Point_1'],points['Point_2'],points['Point_3']]

    depths = [0.0, 10.0, 50.0, 100.0]

    TimeMultiPoint.TIME_DELTA_MIN = timedelta(hours=3)
    TimeMultiPoint.TIME_DELTA_MAX = timedelta(hours=6)

    reader =  SYMPHONIEReader('/work/sciences/projects/WWB-2017/Manicouagan/configuration_V2015/TStra_N/OFFLINE/grid.nc',
                             '/work/sciences/projects/WWB-2017/Manicouagan/configuration_V2015/TStra_N/GRAPHIQUES/20090301_071217.nc',
                              stationCoords,
                              depths)

    # TimeLevel
    myPoints = TimeLevelMultiPoint(reader)
    writer = NcWriter(myPoints, '/tmp/symphonie_points.nc')
    writer.write_variable_sea_surface_height_above_mean_sea_level()
    writer.write_variable_sea_water_temperature()
    writer.write_variable_sea_water_salinity()
    writer.write_variable_baroclinic_sea_water_velocity()
    writer.close()

    print('End of program')




