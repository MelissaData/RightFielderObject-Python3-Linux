import mdRightFielder_pythoncode
import os
import sys
import json


class DataContainer:
    def __init__(self, input="", result_codes=[]):
        self.input = input
        self.result_codes = result_codes

class RightFielderObject:
    """ Set license string and set path to data files  (.dat, etc) """
    def __init__(self, license, data_path):
        self.md_right_fielder_obj = mdRightFielder_pythoncode.mdRightFielder()
        self.md_right_fielder_obj.SetLicenseString(license)
        self.data_path = data_path

        """
        If you see a different date than expected, check your license string and either download the new data files or use the Melissa Updater program to update your data files.
        """
        self.md_right_fielder_obj.SetPathToRightFielderFiles(data_path)
        p_status = self.md_right_fielder_obj.InitializeDataFiles()

        if (p_status != mdRightFielder_pythoncode.ProgramStatus.NoError):
            print("Failed to Initialize Object.")
            print(p_status)
            return
        
        print(f"                DataBase Date: {self.md_right_fielder_obj.GetDatabaseDate()}")
        print(f"              Expiration Date: {self.md_right_fielder_obj.GetLicenseExpirationDate()}")
      
        """
        This number should match with file properties of the Melissa Object binary file.
        If TEST appears with the build number, there may be a license key issue.
        """
        print(f"               Object Version: {self.md_right_fielder_obj.GetBuildNumber()}\n")
    

    def execute_object_and_result_codes(self, data):

        """
        These are the configuarble pieces of the Right Fielder Object. We are setting what kind of information we want to be looked up
        SetUserPattern Method - Ex. Social Security Number

        mdRightFielder.SetUserPattern("SSN", "[0-9]{3}-[0-9]{2}-[0-9]{4}");
        """ 
        self.md_right_fielder_obj.Parse(data.input)
        result_codes = self.md_right_fielder_obj.GetResults()
        

        """ 
        ResultsCodes explain any issues Right Fielder Object has with the object.
        List of result codes for Right Fielder Object
        https://wiki.melissadata.com/?title=Result_Code_Details#RightFielder_Object
        """

        return DataContainer(data.input, result_codes)


def parse_arguments():
    license, test_input, data_path = "", "", ""

    args = sys.argv
    index = 0
    for arg in args:
        
        if (arg == "--license") or (arg == "-l"):
            if (args[index+1] != None):
                license = args[index+1]
        if (arg == "--rfinput") or (arg == "-p"):
            if (args[index+1] != None):
                test_input = args[index+1]
        if (arg == "--dataPath") or (arg == "-d"):
            if (args[index+1] != None):
                data_path = args[index+1]
        index += 1

    return (license, test_input, data_path)

def run_as_console(license, test_input, data_path):
    print("\n\n=========== WELCOME TO MELISSA RIGHT FIELDER OBJECT LINUX PYTHON3 ============\n")

    right_fielder_object = RightFielderObject(license, data_path)

    should_continue_running = True

    if right_fielder_object.md_right_fielder_obj.GetInitializeErrorString() != "No Error":
      should_continue_running = False
      
    while should_continue_running:
        if test_input == None or test_input == "":        
          print("\nFill in each value to see the Right Fielder Object results")
          rf_input = str(input("Right Fielder Input: "))
        else:        
          rf_input = test_input
        
        data = DataContainer(rf_input)

        """ Print user input """
        print("\n================================== INPUTS ====================================\n")
        print(f"\t           Right Fielder Input: {rf_input}")
        # print("\t               Address: {data.Address}")
        # print("\t          CityStateZip: {data.CityStateZip}")
        # print("\t               Company: {data.Company}")
        # print("\t               Country: {data.Country}")
        # print("\t            Department: {data.Department}")
        # print("\t                 Email: {data.Email}")
        # print("\t              FullName: {data.FullName}")
        # print("\t                 Phone: {data.Phone}")
        # print("\t                   Url: {data.Url}")


        """ Execute Right Fielder Object """
        data_container = right_fielder_object.execute_object_and_result_codes(data)

        """ Print output """
        print("\n================================== OUTPUT ====================================\n")
        print("\n\tRight Fielder Object Information:")

        # print(f"\t   Right Fielder Input: {dataContainer.Input}")
        print(f"\t        Address Line 1: {right_fielder_object.md_right_fielder_obj.GetAddress()}")
        print(f"\t        Address Line 2: {right_fielder_object.md_right_fielder_obj.GetAddress2()}")
        print(f"\t        Address Line 3: {right_fielder_object.md_right_fielder_obj.GetAddress3()}")
        print(f"\t                  City: {right_fielder_object.md_right_fielder_obj.GetCity()}")
        print(f"\t                 State: {right_fielder_object.md_right_fielder_obj.GetState()}")
        print(f"\t                   Zip: {right_fielder_object.md_right_fielder_obj.GetPostalCode()}")
        print(f"\t          Result Codes: {data_container.result_codes}")

        # right_fielder_object.md_right_fielder_obj.GetFullNameNext()
        # print(f"\t              FullName: {right_fielder_object.md_right_fielder_obj.GetFullName()}")
        # right_fielder_object.md_right_fielder_obj.GetDepartmentNext()
        # print(f"\t            Department: {right_fielder_object.md_right_fielder_obj.GetDepartment()}")
        # right_fielder_object.md_right_fielder_obj.GetCompanyNext()
        # print(f"\t               Company: {right_fielder_object.md_right_fielder_obj.GetCompany()}")
        # print(f"\t               Country: {right_fielder_object.md_right_fielder_obj.GetCountry()}")
        # print(f"\t              LastLine: {right_fielder_object.md_right_fielder_obj.GetLastLine()}")
        # right_fielder_object.md_right_fielder_obj.GetPhoneNext()
        # print(f"\t                 Phone: {right_fielder_object.md_right_fielder_obj.GetPhone()}")
        # right_fielder_object.md_right_fielder_obj.GetPhoneTypeNext()
        # print(f"\t             PhoneType: {right_fielder_object.md_right_fielder_obj.GetPhoneType()}")
        # right_fielder_object.md_right_fielder_obj.GetEmailNext()
        # print(f"\t                 Email: {right_fielder_object.md_right_fielder_obj.GetEmail()}")
        # right_fielder_object.md_right_fielder_obj.GetURLNext()
        # print(f"\t                   Url: {right_fielder_object.md_right_fielder_obj.GetURL()}")
        # right_fielder_object.md_right_fielder_obj.GetUserFieldNext("SSN")
        # print(f"\t             UserField: {right_fielder_object.md_right_fielder_obj.GetUserField('SSN')}")
        # right_fielder_object.md_right_fielder_obj.GetUnrecognizedNext()
        # print(f"\t          Unrecognized: {right_fielder_object.md_right_fielder_obj.GetUnrecognized()}")



        rs = data_container.result_codes.split(',')
        for r in rs:
            print(f"        {r}: {right_fielder_object.md_right_fielder_obj.GetResultCodeDescription(r, mdRightFielder_pythoncode.ResultCdDescOpt.ResultCodeDescriptionLong)}")


        is_valid = False
        if not (test_input == None or test_input == ""):
            is_valid = True
            should_continue_running = False    
        while not is_valid:
        
            test_another_response = input(str("\nTest Right Fielder Again? (Y/N)\n"))
            

            if not (test_another_response == None or test_another_response == ""):         
                test_another_response = test_another_response.lower()
            if test_another_response == "y":
                is_valid = True
            
            elif test_another_response == "n":
                is_valid = True
                should_continue_running = False            
            else:
            
              print("Invalid Response, please respond 'Y' or 'N'")

    print("\n================== THANK YOU FOR USING MELISSA PYTHON3 OBJECT ================\n")
    


"""  MAIN STARTS HERE   """

license, test_input, data_path = parse_arguments()

run_as_console(license, test_input, data_path)