## TrackerUser - Base User Class
01. username
02. email
03. first_name
04. last_name
05. street_address1
06. street_address2
07. city = ForeignKey(City/Province)
08. postal_code
09. latitude
10 longitude
11. get_email_alerts
12. get_sms_alerts
13. call_IVR_alarm
14. sms_telephone 
15. authorization 
16. min_gelsin_areas
17. sms_end_date
18. grouping_tools
19. is_active
20. is_admin - default no 
21. is_superuser - default no

## Student - Subclass of TrackerUser
1. school ForeignKey(School)  
2. primary_emergency_contact_first_name  
3. primary_emergency_contact_last_name   
4. primary_emergency_phone_sms                                   
5. secondary_emergency_contact_first_name  
6. secondary_emergency_contact_last_name   
7. secondary_emergency_phone_sms                                    
8. is_student_verified  

## Driver - Subclass of TrackerUser
1. has_ignition_locking_auth 
2. license_issue_date
3. license_expiration_date 

## SchoolManager - Subclass of TrackerUser
1. is_school_staff 
2. school ForeignKey(School)
3. position_title

## AdminManager - Subclass of TrackerUser
1. admin_title
