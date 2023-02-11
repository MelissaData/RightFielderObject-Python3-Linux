from ctypes import *
from enum import Enum
import ctypes
import os

dir = os.getcwd()

if (os.name == 'nt'):
  lib = ctypes.CDLL(f'{dir}/MelissaRightFielderObjectWindowsPython3/mdRightFielder.dll')
else:
  lib = ctypes.CDLL(f'{dir}/MelissaRightFielderObjectLinuxPython3/libmdRightFielder.so')

lib.mdRightFielderCreate.argtypes = []
lib.mdRightFielderCreate.restype = c_void_p
lib.mdRightFielderDestroy.argtypes = [c_void_p]
lib.mdRightFielderDestroy.restype = None
lib.mdRightFielderSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderSetLicenseString.restype = c_bool
lib.mdRightFielderSetPathToRightFielderFiles.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderSetPathToRightFielderFiles.restype = None
lib.mdRightFielderGetBuildNumber.argtypes = [c_void_p]
lib.mdRightFielderGetBuildNumber.restype = c_char_p
lib.mdRightFielderGetDatabaseDate.argtypes = [c_void_p]
lib.mdRightFielderGetDatabaseDate.restype = c_char_p
lib.mdRightFielderGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdRightFielderGetLicenseExpirationDate.restype = c_char_p
lib.mdRightFielderInitializeDataFiles.argtypes = [c_void_p]
lib.mdRightFielderInitializeDataFiles.restype = c_int
lib.mdRightFielderGetInitializeErrorString.argtypes = [c_void_p]
lib.mdRightFielderGetInitializeErrorString.restype = c_char_p
lib.mdRightFielderSetDelimiter.argtypes = [c_void_p, c_int]
lib.mdRightFielderSetDelimiter.restype = None
lib.mdRightFielderSetAcceptFullName.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptFullName.restype = None
lib.mdRightFielderSetAcceptDepartment.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptDepartment.restype = None
lib.mdRightFielderSetAcceptCompany.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptCompany.restype = None
lib.mdRightFielderSetAcceptAddress.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptAddress.restype = None
lib.mdRightFielderSetAcceptCityStateZip.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptCityStateZip.restype = None
lib.mdRightFielderSetAcceptCountry.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptCountry.restype = None
lib.mdRightFielderSetAcceptPhone.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptPhone.restype = None
lib.mdRightFielderSetAcceptEmail.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptEmail.restype = None
lib.mdRightFielderSetAcceptURL.argtypes = [c_void_p, c_bool]
lib.mdRightFielderSetAcceptURL.restype = None
lib.mdRightFielderSetUserPattern.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdRightFielderSetUserPattern.restype = c_bool
lib.mdRightFielderParse.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderParse.restype = c_bool
lib.mdRightFielderParseFreeForm.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderParseFreeForm.restype = c_bool
lib.mdRightFielderParseFielded.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderParseFielded.restype = c_bool
lib.mdRightFielderGetFullName.argtypes = [c_void_p]
lib.mdRightFielderGetFullName.restype = c_char_p
lib.mdRightFielderGetFullNameNext.argtypes = [c_void_p]
lib.mdRightFielderGetFullNameNext.restype = c_bool
lib.mdRightFielderGetDepartment.argtypes = [c_void_p]
lib.mdRightFielderGetDepartment.restype = c_char_p
lib.mdRightFielderGetDepartmentNext.argtypes = [c_void_p]
lib.mdRightFielderGetDepartmentNext.restype = c_bool
lib.mdRightFielderGetCompany.argtypes = [c_void_p]
lib.mdRightFielderGetCompany.restype = c_char_p
lib.mdRightFielderGetCompanyNext.argtypes = [c_void_p]
lib.mdRightFielderGetCompanyNext.restype = c_bool
lib.mdRightFielderGetAddress.argtypes = [c_void_p]
lib.mdRightFielderGetAddress.restype = c_char_p
lib.mdRightFielderGetAddress2.argtypes = [c_void_p]
lib.mdRightFielderGetAddress2.restype = c_char_p
lib.mdRightFielderGetAddress3.argtypes = [c_void_p]
lib.mdRightFielderGetAddress3.restype = c_char_p
lib.mdRightFielderGetCity.argtypes = [c_void_p]
lib.mdRightFielderGetCity.restype = c_char_p
lib.mdRightFielderGetState.argtypes = [c_void_p]
lib.mdRightFielderGetState.restype = c_char_p
lib.mdRightFielderGetPostalCode.argtypes = [c_void_p]
lib.mdRightFielderGetPostalCode.restype = c_char_p
lib.mdRightFielderGetCountry.argtypes = [c_void_p]
lib.mdRightFielderGetCountry.restype = c_char_p
lib.mdRightFielderGetLastLine.argtypes = [c_void_p]
lib.mdRightFielderGetLastLine.restype = c_char_p
lib.mdRightFielderGetPhone.argtypes = [c_void_p]
lib.mdRightFielderGetPhone.restype = c_char_p
lib.mdRightFielderGetPhoneNext.argtypes = [c_void_p]
lib.mdRightFielderGetPhoneNext.restype = c_bool
lib.mdRightFielderGetPhoneType.argtypes = [c_void_p]
lib.mdRightFielderGetPhoneType.restype = c_char_p
lib.mdRightFielderGetPhoneTypeNext.argtypes = [c_void_p]
lib.mdRightFielderGetPhoneTypeNext.restype = c_bool
lib.mdRightFielderGetEmail.argtypes = [c_void_p]
lib.mdRightFielderGetEmail.restype = c_char_p
lib.mdRightFielderGetEmailNext.argtypes = [c_void_p]
lib.mdRightFielderGetEmailNext.restype = c_bool
lib.mdRightFielderGetURL.argtypes = [c_void_p]
lib.mdRightFielderGetURL.restype = c_char_p
lib.mdRightFielderGetURLNext.argtypes = [c_void_p]
lib.mdRightFielderGetURLNext.restype = c_bool
lib.mdRightFielderGetUserField.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderGetUserField.restype = c_char_p
lib.mdRightFielderGetUserFieldNext.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderGetUserFieldNext.restype = c_bool
lib.mdRightFielderGetUnrecognized.argtypes = [c_void_p]
lib.mdRightFielderGetUnrecognized.restype = c_char_p
lib.mdRightFielderGetUnrecognizedNext.argtypes = [c_void_p]
lib.mdRightFielderGetUnrecognizedNext.restype = c_bool
lib.mdRightFielderGetResults.argtypes = [c_void_p]
lib.mdRightFielderGetResults.restype = c_char_p
lib.mdRightFielderGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdRightFielderGetResultCodeDescription.restype = c_char_p
lib.mdRightFielderSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdRightFielderSetReserved.restype = None
lib.mdRightFielderGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdRightFielderGetReserved.restype = c_char_p

# mdRightFielder Enumerations
class ProgramStatus(Enum):
	NoError = 0
	ConfigFile = 1
	LicenseExpired = 2
	Unknown = 4

class Delimiter(Enum):
	Tab = 0
	Comma = 1
	Pipe = 2
	CRLF = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class mdRightFielder(object):
	def __init__(self):
		self.I = lib.mdRightFielderCreate()

	def __del__(self):
		lib.mdRightFielderDestroy(self.I)

	def SetLicenseString(self, p1):
		return lib.mdRightFielderSetLicenseString(self.I, p1.encode('utf-8'))

	def SetPathToRightFielderFiles(self, p1):
		lib.mdRightFielderSetPathToRightFielderFiles(self.I, p1.encode('utf-8'))

	def GetBuildNumber(self):
		return lib.mdRightFielderGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdRightFielderGetDatabaseDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		return lib.mdRightFielderGetLicenseExpirationDate(self.I).decode('utf-8')

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdRightFielderInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdRightFielderGetInitializeErrorString(self.I).decode('utf-8')

	def SetDelimiter(self, p1):
		lib.mdRightFielderSetDelimiter(self.I, Delimiter(p1).value)

	def SetAcceptFullName(self, p1):
		lib.mdRightFielderSetAcceptFullName(self.I, p1)

	def SetAcceptDepartment(self, p1):
		lib.mdRightFielderSetAcceptDepartment(self.I, p1)

	def SetAcceptCompany(self, p1):
		lib.mdRightFielderSetAcceptCompany(self.I, p1)

	def SetAcceptAddress(self, p1):
		lib.mdRightFielderSetAcceptAddress(self.I, p1)

	def SetAcceptCityStateZip(self, p1):
		lib.mdRightFielderSetAcceptCityStateZip(self.I, p1)

	def SetAcceptCountry(self, p1):
		lib.mdRightFielderSetAcceptCountry(self.I, p1)

	def SetAcceptPhone(self, p1):
		lib.mdRightFielderSetAcceptPhone(self.I, p1)

	def SetAcceptEmail(self, p1):
		lib.mdRightFielderSetAcceptEmail(self.I, p1)

	def SetAcceptURL(self, p1):
		lib.mdRightFielderSetAcceptURL(self.I, p1)

	def SetUserPattern(self, p1, p2):
		return lib.mdRightFielderSetUserPattern(self.I, p1.encode('utf-8'), p2.encode('utf-8'))

	def Parse(self, p1):
		return lib.mdRightFielderParse(self.I, p1.encode('utf-8'))

	def ParseFreeForm(self, p1):
		return lib.mdRightFielderParseFreeForm(self.I, p1.encode('utf-8'))

	def ParseFielded(self, p1):
		return lib.mdRightFielderParseFielded(self.I, p1.encode('utf-8'))

	def GetFullName(self):
		return lib.mdRightFielderGetFullName(self.I).decode('utf-8')

	def GetFullNameNext(self):
		return lib.mdRightFielderGetFullNameNext(self.I)

	def GetDepartment(self):
		return lib.mdRightFielderGetDepartment(self.I).decode('utf-8')

	def GetDepartmentNext(self):
		return lib.mdRightFielderGetDepartmentNext(self.I)

	def GetCompany(self):
		return lib.mdRightFielderGetCompany(self.I).decode('utf-8')

	def GetCompanyNext(self):
		return lib.mdRightFielderGetCompanyNext(self.I)

	def GetAddress(self):
		return lib.mdRightFielderGetAddress(self.I).decode('utf-8')

	def GetAddress2(self):
		return lib.mdRightFielderGetAddress2(self.I).decode('utf-8')

	def GetAddress3(self):
		return lib.mdRightFielderGetAddress3(self.I).decode('utf-8')

	def GetCity(self):
		return lib.mdRightFielderGetCity(self.I).decode('utf-8')

	def GetState(self):
		return lib.mdRightFielderGetState(self.I).decode('utf-8')

	def GetPostalCode(self):
		return lib.mdRightFielderGetPostalCode(self.I).decode('utf-8')

	def GetCountry(self):
		return lib.mdRightFielderGetCountry(self.I).decode('utf-8')

	def GetLastLine(self):
		return lib.mdRightFielderGetLastLine(self.I).decode('utf-8')

	def GetPhone(self):
		return lib.mdRightFielderGetPhone(self.I).decode('utf-8')

	def GetPhoneNext(self):
		return lib.mdRightFielderGetPhoneNext(self.I)

	def GetPhoneType(self):
		return lib.mdRightFielderGetPhoneType(self.I).decode('utf-8')

	def GetPhoneTypeNext(self):
		return lib.mdRightFielderGetPhoneTypeNext(self.I)

	def GetEmail(self):
		return lib.mdRightFielderGetEmail(self.I).decode('utf-8')

	def GetEmailNext(self):
		return lib.mdRightFielderGetEmailNext(self.I)

	def GetURL(self):
		return lib.mdRightFielderGetURL(self.I).decode('utf-8')

	def GetURLNext(self):
		return lib.mdRightFielderGetURLNext(self.I)

	def GetUserField(self, p1):
		return lib.mdRightFielderGetUserField(self.I, p1.encode('utf-8')).decode('utf-8')

	def GetUserFieldNext(self, p1):
		return lib.mdRightFielderGetUserFieldNext(self.I, p1.encode('utf-8'))

	def GetUnrecognized(self):
		return lib.mdRightFielderGetUnrecognized(self.I).decode('utf-8')

	def GetUnrecognizedNext(self):
		return lib.mdRightFielderGetUnrecognizedNext(self.I)

	def GetResults(self):
		return lib.mdRightFielderGetResults(self.I).decode('utf-8')

	def GetResultCodeDescription(self, resultCode, opt):
		return lib.mdRightFielderGetResultCodeDescription(self.I, resultCode.encode('utf-8'), ResultCdDescOpt(opt).value).decode('utf-8')

	def SetReserved(self, p1, p2):
		lib.mdRightFielderSetReserved(self.I, p1.encode('utf-8'), p2.encode('utf-8'))

	def GetReserved(self, p1):
		return lib.mdRightFielderGetReserved(self.I, p1.encode('utf-8')).decode('utf-8')
