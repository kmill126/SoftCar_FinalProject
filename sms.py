"""
Python 3.7.2
Katherine Miller
Final Project

sms.py will send a text message to any cell phone using
the carrier and gmail smtp gateways

-------------Cell Carrier Emails-----------------
T-Mobile:      phonenumber@tmomail.net
Virgin Mobile: phonenumber@vmobl.com
Cingular:      phonenumber@cingularme.com
Sprint:        phonenumber@messaging.sprintpcs.com
Verizon:       phonenumber@vtext.com
Nextel:        phonenumber@messaging.nextel.com
Att:           phonenumber@mms.att.net

"""

import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()

# Gmail account with which to set up secure session
# Make sure account > security > unsecure app access is turned on
# Otherwise will get a password incorrect error
server.login( 'SoftwareCarpentry1@gmail.com', 'SoftCar1' )


msg = "Hello from Python!"

# Send message via carrier SMS gateway
server.sendmail( 'SoftwareCarpentry1', '6099543460@mms.att.net', msg )
