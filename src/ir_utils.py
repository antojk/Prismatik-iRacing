#
# Project     Prismatik - iRacing Plugin
# @author     David Madison
# @link       github.com/dmadison/Prismatik-iRacing
# @license    GPLv3 - Copyright (c) 2017 David Madison
#
# This file is part of the Prismatik - iRacing Plugin.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import irsdk
from whitelist import irvar_whitelist as whitelist


class iRacer:
	def __init__(self):
		self.api = irsdk.IRSDK()
		self.__connected = False

		# Shift Light Information
		self.__shift_rpm = 6000
		self.__shift_rpm_min = 0
		self.__shift_rpm_max = 6000
		self.__shift_rpm_max_blink = 6250

		self.api.startup()

	def __check_api_state(self):
		if self.api.is_initialized and self.api.is_connected:
			return True
		else:
			self.api.startup()
			return False

	def check_connection(self):
		api_status = self.__check_api_state()

		if self.__connected and not api_status:
			self.__connected = False
			self.api.shutdown()
			print('irsdk disconnected')
			return 'Disconnected'
		elif not self.__connected and api_status:
			self.__connected = True
			print('irsdk connected')
			self.__get_shift_points()
			return 'Connected'
		else:
			return api_status

	def get_data(self, var):
		if var == 'ShiftLight':
			return self.sli_percent()
		elif var == 'ShiftLightBlink':
			return self.sli_blink()
		else:
			return self.api[var]

	def __get_shift_points(self):
		self.__shift_rpm = self.api['DriverInfo']['DriverCarSLShiftRPM']
		self.__shift_rpm_min = self.api['DriverInfo']['DriverCarSLFirstRPM']
		self.__shift_rpm_max = self.api['DriverInfo']['DriverCarSLLastRPM']
		self.__shift_rpm_max_blink = self.api['DriverInfo']['DriverCarSLBlinkRPM']

	def sli_percent(self):
		rpm_max_scale = self.__shift_rpm_max - self.__shift_rpm_min

		rpm_current = self.api['RPM']

		if rpm_current >= self.__shift_rpm_max_blink:
			return 1.01
		elif rpm_current >= self.__shift_rpm_max:
			return 1.0
		elif rpm_current <= self.__shift_rpm_min:
			return 0.0
		else:
			rpm_current -= self.__shift_rpm_min
			shift_percentage = rpm_current / rpm_max_scale
			return shift_percentage

	def sli_blink(self):
		if self.api['RPM'] >= self.__shift_rpm:
			return 1.01
		else:
			return 0.0
