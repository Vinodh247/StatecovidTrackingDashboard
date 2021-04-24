#!pip install covid-india
#!pip install pywebio
from pywebio.input import *
from pywebio.output import *
from covid_india import states

def findout():
        yourstate = radio("Select state", options=['AndhraPradesh','ArunachalPradesh',	'Assam',	'Bihar',	'Chhattinsgarh',	'Goa',	'Gujarat',	
                                                   'Haryana',	'HimachalPradesh',	'JammuandKashmir',	'Jharkhand',	'Karnataka',	'Kerala',	
                                                   'MadhyaPradesh',	'Maharashtra',	'Manipur',	'Meghalaya',	'Mizoram',	'Nagaland',	'Odisha',	
                                                   'Punjab',	'Rajasthan',	'Sikkim',	'TamilNadu',	'Telangana',	'Tripura',	'Uttarakhand',	
                                                   'UttarPradesh',	'WestBengal',	'AndamanandNicobarIslands',	'Chandigarh',	'DadraandNagarHaveli',	
                                                   'DamanandDiu',	'Delhi',	'Lakshadweep',	'Puducherry'])
        yourstate = radio("Select the required covid info", options=['Active patients','Cured patients','Death'])
        if(yourstate == 'Active patients'):
            outputfound = states.getdata(yourstate)['Active']
        elif(yourstate == 'Cured patients'):
            outputfound = states.getdata(yourstate)['Cured']
        else:
            outputfound = states.getdata(yourstate)['Death']
          
            put_text('the option selected is '+yourstate+ ' ' +str(outputfound))
#put_text(yourstate)

if __name__ == '__main__':
    findout()