import os
import json
import subprocess
#import pyttsx3 as pt

os.system("tput setaf 6")
while True:
    print("--------------------------------------------------------------------------------------------- WELCOME! TO AUTOMATION WORLD! --------------------------------------------------------------------------------------- ")
    #pt.speak("Welcome ! To Automation World!")
    print("""\n\n--------------------------------------------------------------------------------------------------- SERVICES AVAILABLE --------------------------------------------------------------------------------------------
            \n\t\t\t\t\t\t\t\t\t\t\t1. DO YOU WANT TO USE **AWS SERVICES**
            \t\t\t\t\t\t\t\t\t\t2. HADOOP SERVICES
            \t\t\t\t\t\t\t\t\t\t3. DOCKER SEVICES
            \t\t\t\t\t\t\t\t\t\t4. WEBSERVER SERVICES
            \t\t\t\t\t\t\t\t\t\t5. Automating LVM Partition using Python-Script
            \t\t\t\t\t\t\t\t\t\t6. Exit From Automation World
            \n\n""")
    #pt.speak("Hello! Myself Gloomy! I Am Capable Of Automating The Things And Making Your Life Easy. Here Are Some Services Which I Can Do For You!")
    #pt.speak("1. Do You Want To Use Aws Services")
    #pt.speak("2. Do You Want To Go For Haddop Services")
    #pt.speak("3. Do You Want To Go For Docker Services")
    #pt.speak("4. Do You Want To Go For Webserver Services")
    #pt.speak("5. Do You Want To Automate LVM Partition Using Python-Script")
    #pt.speak("6. Do You Want To Exit From Automtion World!")
    option = int(input("ENTER YOUR CHOICE : "))
    #pt.speak("Enter You Choice :")
    if option == 1:
        print("---->>>Enter AWS account Access Key , Secret Key , Region and choose JSON language")
        print("\n Do you want to login into aws account ? press y or n:", end='')
        #pt.speak("Do You Want To Login into aws account If Yes Then Press Y Or Else N")
        login_aws = input()
        if login_aws == 'y':
            os.system("aws configure")
            while True:
                print("""
                        CHOOSE THE SERVICES OF AWS- 
                        PRESS:
                             1. EC2
                             2. EBS
                             3. S3
                             4. CloudFront
                    """)
               # pt.speak("Choose The Services Of AWS From Follwing Menu Given Below")
                #pt.speak("Press 1 For Using EC2 Service")
                #pt.speak("Press 2 For Using EBS Service")
                #pt.speak("Press 3 For Using S3 Service")
                #pt.speak("Press 4 For Using Cloud Front Service")

                service = int(input("Enter Your Choice From Above Menu :"))
                if service == 1:
                    print("""
                                    PRESS:
                                         1. LAUNCH THE EC2-INSTANCE
                                         2. START THE EXISTING EC2-INSTANCE
                                         3. DELETE THE EC2-INSTANCE
                                         4. ALL INFO ABOUT ALL EC2-INSTANCES 
                        """)
                    print("Enter Your Choice From Above Menu : ", end='')
                    ec2_input = int(input())
                    if ec2_input == 1:
                        print("""
                                            PRESS:
                                                 1. For Creating new key
                                                 2. For Using the existing key
                                    """)
                        key = int(input("Enter Your Choice From Above Menu :"))
                        if key == 1:
                            key_name = input("Enter key name : ")
                            os.system(
                                '''aws ec2 create-key-pair --key-name {0} --query "KeyMaterial" --output text > {0}.ppk'''.format(key_name))
                            os.system("chmod 400 {}.ppk".format(key_name))
                        else:
                            key_name = input(
                                "Enter key name [make sure the spelling is correct] : ")
                        # SECURITY GROUP
                        print("""
                                            PRESS:
                                                 1. CREATE SECURITY GROUP
                                                 2. USE EXISTING SECURITY GROUP
                                    """)
                        security = int(
                            input("Enter Your Choice From Above Menu :"))
                        if security == 1:
                            security_group_name = input(
                                "Enter security group name : ")
                            security_description = input(
                                "Enter Security Group Description : ")
                            x = subprocess.getstatusoutput(
                                "aws ec2 create-security-group --group-name {} --description {} ".format(security_group_name, security_description))
                            y = json.loads(x[1])
                            security_group_id = y.get('GroupId')
                        elif security == 2:

                            security_group_id = input(
                                "ENTER SECURITY GROUP ID : ")
                        # IMAGE FOR  OS
                        print("""
                                            SELECT THE IMAGE FOR LAUNCHING THE OS- 
                                                PRESS:
                                                     1. Amazon Linux 2 AMI (HVM)
                                                     2. Red Hat Enterprise Linux 8 (HVM)
                                                     3. SUSE Linux Enterprise Server 15 SP2 (HVM)
                                                     4. Ubuntu Server 20.04 LTS (HVM)
                                                     5. Microsoft Windows Server 2019 Base
                                    """)
                        image = int(
                            input("Enter Your Choice From Above Menu : "))
                        if image == 1:
                            image_id = "ami-0947d2ba12ee1ff75"
                        elif image == 2:
                            image_id = "ami-098f16afa9edf40be"
                        elif image == 3:
                            image_id = "ami-0a782e324655d1cc0"
                        elif image == 4:
                            image_id = "ami-0dba2cb6798deb6d8"
                        elif image == 5:
                            image_id = "ami-0412e100c0177fb4b"
                        else:
                            print(
                                "Your Choice Is Invalid ! Please Check It And Try Again !")
                        # INSTANCE TYPE
                        print("""
                                            Choose an Instance Type-
                                                PRESS:
                                                     1. t2.nano
                                                     2. t2.micro
                                                     3. t2.small
                                                     4. t2.medium
                                                     5. t2.large
                                    """)
                        instance_type_no = int(
                            input("Enter Your Choice From Above Menu : "))
                        if instance_type_no == 1:
                            instance_type = "t2.nano"
                        elif instance_type_no == 2:
                            instance_type = "t2.micro"
                        elif instance_type_no == 3:
                            instance_type = "t2.small"
                        elif instance_type_no == 4:
                            instance_type = "t2.medium"
                        elif instance_type_no == 5:
                            instance_type = "t2.large"
                        # COUNT
                        no_of_instance = input(
                            "Enter Number of Instances You Would Like To Launch : ")
                        # SELECT SUBNET
                        subnet_id = input("Enter Subnet Id :")
                        os.system("aws ec2 run-instances --image-id {0} --count {1} --instance-type {2} --key-name {3} --security-group-ids {4} --subnet-id {5}".format(
                            image_id, no_of_instance, instance_type, key_name, security_group_id, subnet_id))

                        print("""
            -----------------------------------------------------NEW INSTANCE LAUNCHED------------------------------------------------------------------------
                            
                                    """)
                        #action = int(input("Please Choose Any One Option From Above Menu : "))
                        # if action == 1:
                        #   #os.chdir(r"C:\Users\rhyth\Desktop\python_programs")
                        #  ip = input("ENTER THE PUBLIC IP [SEE FROM THE AWS CONSOLE DASHBOARD]")
                        # os.system("ssh -i {}.ppk ec2-user@{}".format(key_name,ip))
                    elif ec2_input == 2:
                        instance_id = input(
                            "Enter The Correct Instance ID To Start EC2 Instance : ")
                        os.system(
                            "aws ec2 start-instances --instance-ids {}".format(instance_id))
                        print("""
            -----------------------------------------------------INSTANCE HAS BEEN STARTED------------------------------------------------------------------------
                    
                                """)
                        #action = int(input())
                        # if action == 1:
                        # os.chdir(r"C:\Users\rhyth\Desktop\python_programs")
                        #           ip = input("ENTER THE PUBLIC IP [SEE FROM THE AWS CONSOLE DASHBOARD]")
                        #          key_name = input("enter key name")
                        #         os.system("ssh -i {0}.ppk ec2-user@{1}".format(key_name,ip))
                    elif ec2_input == 3:
                        print("""
                                    Do YOU WANT TO -
                                         1. TERMINATE THE EC2 INSTANCE
                                         2. STOP THE EC2 INSTANCE
                                """)
                       # pt.speak("Do You Want To Terminate The Ec2 Instance Then Press 1. Do You Want Stop The EC2 Instance Then Press 2.")
                        del_ter = int(input("ENTER YOUR CHOICE FROM ABOVE MENU : "))
                        if del_ter == 1:
                            Instance_id = input(
                                "Enter Instance Id To Terminate The EC2 Instance : ")
                            os.system(
                                "aws ec2 terminate-instances --instance-ids {}".format(Instance_id))
                        else:
                            Instance_id = input(
                                "Enter Instance Id To Stop The EC2 Instance : ")
                            os.system(
                                "aws ec2 stop-instances  --instance-ids {}".format(Instance_id))
                    else:
                        os.system("aws ec2 describe-instances")
                    print("\n\nDO YOU WANT TO CONTINUE USING EC2 SERVICES ? if Yes press 'y' or No press 'n' : ", end='')
                    choice = input()
                    if choice == "y":
                        pass
                    else:
                        break
                elif service == 2:
                    os.system("tput setaf 6")
                    while True:
                        print("----------------------------------------WELCOME TO EBS SERVICES--------------------------------------- ")
                        print("""
                                CHOOSE WHAT YOU WOULD LIKE TO DO WITH EBS :
                                PRESS :
                                    1. Create a New EBS
                                    2. Show Existing Volumes Information
                                    3. Show Existing EC2 Information
                                    4. Attach EBS With Instance
                                    5. Deattach EBS With Instance
                                    6. Delete EBS 
                                    7. Exit From EBS Menu
                    """)
                        print()
                        print(
                            "Hello! Myself Gloomy. Please Type Any One Option From Above Menu : ", end='')

                        ebs_choice = input()
                        if ebs_choice == '1':
                            print("""
                                Volume Types Are :
                                        * gp2 (General Purpose SSD)
                                        * io1 (Provisioned IOPS SSD)
                                        * io2 (Provisioned IOPS SSD)
                                        * sc1 (Cold HDD)
                                        * st1 (Throughput Optimized HDD)
                                        * standard (Magnetic)
                                """)
                            print(
                                "Enter Volume Type like 'gp2' According To Your Use Case : ", end='')
                            volume_type = input().lower()
                            print("Enter Volume Size In GiB : ", end='')
                            volume_size = int(input())
                            print("Enter Availability Zone : ", end='')
                            a_zone = input().lower()
                           # print("Enter Volume Name : ",end='')
                            #volume_name = input().capitalize()
                            os.system("tput setaf 2")
                            os.system("aws ec2 create-volume --volume-type {0} --size {1} --availability-zone {2}".format(
                                volume_type, volume_size, a_zone))
                            os.system("tput setaf 6")

                        elif ebs_choice == '2':
                            os.system("tput setaf 2")
                            os.system("aws ec2 describe-volumes")
                            os.system("tput setaf 6")

                        elif ebs_choice == '3':
                            os.system("tput setaf 2")
                            os.system("aws ec2 describe-instances")
                            os.system("tput setaf 6")

                        elif ebs_choice == '4':
                            print("Enter Volume Id To Continue : ", end='')
                            vol_id = input().lower()
                            print(
                                "Enter Instance Id With Whome You Like To Attach With : ", end='')
                            insta_id = input().lower()
                            print(
                                "Enter Device Name Of That Volume To Be Attached : ", end='')
                            device_name = input()
                            os.system("tput setaf 2")
                            os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}".format(
                                vol_id, insta_id, device_name))
                            print("You Attached EBS Volume  ")
                            os.system("tput setaf 6")

                        elif ebs_choice == '5':
                            print("Enter Volume Id To Deattach Volume : ", end='')
                            volume_id = input().lower()
                            os.system("tput setaf 2")
                            os.system(
                                "aws ec2 detach-volume --volume-id {0}".format(volume_id))
                            os.system("tput setaf 6")

                        elif ebs_choice == '6':
                            print(
                                "Enter The Volume Id To Delete The EBS Volume : ", end='')
                            volume_id = input().lower()
                            os.system(
                                "aws ec2 delete-volume --volume-id {0}".format(volume_id))
                            os.system("tput setaf 2")
                            print("Volume Deleted Successfully.")
                            os.system("tput setaf 6")

                        elif ebs_choice == '7':
                            break

                        else:
                            os.system("tput setaf 1")
                            print(
                                "Please Choose Valid Option From Menu! Invalid Choice! Try Again!")
                            os.system("tput setaf 6")

                elif service == 3:
                    while True:
                        #print("s3 services")
                        #import os
                        print(
                            "----------------------------WELCOME TO S3 SERVICES----------------------------------------------")
                        print(""" SELECT :
                                1 : CREATE NEW BUCKET
                                2 : UPLOAD OBJECT IN THE BUCKET
                                3 : SET PERMISSION TO PUBLIC FOR A PARTICULAR OBJECT IN THE BUCKET
                                4 : Exit From Here
                        
                        """)
                        s3_input = int(input())
                        if s3_input == 1:
                            bucket_name = input("ENTER THE BUCKET NAME : ")
                            Region = input("ENTER THE REGION (eg: ap-south-1) : ")
                            os.system(
                                "aws s3api create-bucket --bucket {} --region {}".format(bucket_name, Region))
                            print(
                                "------------------------------BUCKET HAS BEEN CREATED-------------------------------")
                        elif s3_input == 2:
                            bucket_object = input(
                                    "Enter Name of object in the bucket : ")
                            bucket_name = input("Enter bucket name : ")
                            os.system(
                                "aws s3 cp {} s3://{}/".format(bucket_object, bucket_name))
                        elif s3_input == 3:
                            bucket_name = input("Enter bucket name :")
                            bucket_object = input("ENter object name : ")
                            os.system(
                                "aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(bucket_name, bucket_object))
                        elif s3_input ==4:
                            break;
                        else:
                            print("OPTION NOT SUPPORTED")
                    print("WANT TO CONTINUE USING S3 SERVICES? PRESS y if Yes : ")
                    s3_inp = input()
                    if s3_inp == 'y':
                        pass
                    else:
                        break

                elif service == 4:
                    print(
                        "----------------------------WELCOME TO CLOUD FRONT----------------------------------------------")
                    domain_name = input("Enter the Origin Domain Name : ")
                    object_name = input("Enter object name : ")
                    os.system(
                        "aws cloudfront create-distribution --origin-domain-name {} --default-root-object {}".format(domain_name, object_name))

    elif option == 2:
        def core_site():
            file_object = open("/etc/hadoop/core-site.xml", "w")
            ip_of_name_node = input("Enter IP of Name Node")
            L = ['<?xml version="1.0"?>\n', '<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n', '<configuration>\n', '<property>\n',
                    '<name>fs.default.name</name>\n', '<value>hdfs://'+ip_of_name_node+':9001</value>\n', '</property>\n', '</configuration>\n']
            file_object.writelines(L)
            file_object.close()

        def hdfs_site_namenode():
            os.system("mkdir /namenode_ws")
            file_object = open("/etc/hadoop/hdfs-site.xml", "w")
            L = ['<?xml version="1.0"?>\n', '<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n', '<configuration>\n',
                 '<property>\n', '<name>dfs.name.dir</name>\n', '<value>/namenode_ws</value>\n', '<property>\n', '</configuration>\n']
            file_object.writelines(L)
            file_object.close()

        def hdfs_site_datanode():
            os.system("mkdir /datanode_ws")
            file_object = open("/etc/hadoop/hdfs-site.xml", "w")
            L = ['<?xml version="1.0"?>', '<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>', '<configuration>',
                 '<property>', '<name>dfs.data.dir</name>', '<valu>/namenode_ws</value>', '<property>', '</configuration>']
            file_object.writelines(L)
            file_object.close()

        while True:
            print("-----------------------------------------WELCOME TO HADOOP SERVICES------------------------------------")
            print("""
                                WHAT DO YOU WANT TO DO, CHOOSE YOUR OPTION-
                                                1. HADOOP INSTALLATION
                                                2. HADOOP CONFIGURATION and START THE SERVICES
                                                3. SHOW THE HADOOP CLUSTER REPORT {make sure you already installed and configured the Hadoop and start the services }
                                                4. check all the Hadoop daemons
                    """)
            hadoop_choice = int(input("Enter Your Choice From Above : "))
            if hadoop_choice == 1:
                os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
                os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
            elif hadoop_choice == 2:
                print("""
                            do you want to configure it as a :-
                            1 - NAME NODE
                            2 - SLAVE NODE
                            3 - HADOOP CLIENT

                            """)
                node = int(input("Enter your choice: "))
                if node == 1:
                    core_site()
                    hdfs_site_namenode()
                    os.system("hadoop-daemon.sh start namenode")
                elif node == 2:
                    core_site()
                    os.system("hadoop-daemon.sh start datanode")
                    hdfs_site_datanode()
                elif node == 3:
                    core_site()

            elif hadoop_choice == 3:
                os.system("hadoop dfsadmin -report")
            else:
                os.system("jps")

            print("""do you want to coutinue?

                            if yes press : y
                            otherwise press : n

                    """)
            x = input("Enter your choice: ")
            if x == "y":
                pass
            else:
                break
    elif option == 3:
        while True:
            os.system("tput setaf 6")
            print("----------------------------------------WELCOME TO DOCKER SERVICES----------------------------------------------------------------------------- ")
            print("""
                CHOOSE WHAT YOU WOULD LIKE TO DO IN DOCKER :
                PRESS :
                    1. Show Docker Info
                    2. Show Docker Status
                    3. Launch Docker Container
                    4. Start Existing Docker Container
                    5. Show Existing Docker Images
                    6. Show Docker Container Which Are Stopped
                    7. Show Current Status Of Docker Containers
                    8. Search Docker Images Available In Docker Hub
                    9. Download Docker Images
                   10. Copy Files From Base OS to Docker Container
                   11. Copy Files From Docker Container To Base OS
                   12. Stop Docker Container
                   13. Remove Docker Images
                   14. Remove Docker Container
                   15. EXIT From Docker Container
            """)
            print()
            print("Hello! Myself Gloomy. How Can I Help You ?", end='')

            docker_choice = int(input())
            if docker_choice == 1:
                os.system("tput setaf 2")
                os.system("docker info")
                os.system("tput setaf 6")

            elif docker_choice == 2:
                os.system("systemctl status docker")

            elif docker_choice == 3:  # optimize
                print("""
                        CHOOSE WHAT YOU WOULD LIKE TO DO :
                        PRESS :
                            1. Launch Docker Container
                            2. Exit From Launching
                """)
                print("Enter Your Choice : ", end='')
                launch_choice = int(input())
                if launch_choice == 1:
                    print("Ok! For That You Need to Provide Container Name : ", end='')
                    container_name = input()
                    print("After! That You Need to Provide Image Name : ", end='')
                    image_name = input()
                    print("Also! Provide Version Name : ", end='')
                    version_name = input()
                    os.system(
                        "docker run -dit --name {0} {1}:{2}".format(container_name, image_name, version_name))
                    os.system("tput setaf 2")
                    print("Docker Container Launched Successfully")
                    os.system("tput setaf 6")
                elif launch_choice == 2:
                    os.system("tput setaf 3")
                    print(
                        "Ok! We are Exiting You From Docker Launching Menu to Main Menu.")
                    os.system("tput setaf 6")
                    break
                else:
                    os.system("tput setaf 1")
                    print("Please Choose Valid Option From Menu! Invalid Choice!")
                    os.system("tput setaf 6")

            elif docker_choice == 4:  # optimize
                print("To Start U Need To Give Container Name : ", end='')
                cont_name = input()
                os.system("tput setaf 2")
                os.system("docker start {0}".format(cont_name))
                print("Docker Container Started Successfully.")
                os.system("tput setaf 6")

            elif docker_choice == 5:
                os.system("tput setaf 2")
                os.system("docker image ls")
                os.system("tput setaf 6")

            elif docker_choice == 6:
                os.system("tput setaf 2")
                os.system("docker ps -a")
                os.system("tput setaf 6")

            elif docker_choice == 7:
                os.system("tput setaf 2")
                os.system("docker ps")
                os.system("tput setaf 6")

            elif docker_choice == 8:
                print("Enter Image Name To Search On Docker HUB : ", end='')
                search_image = input()
                os.system("tput setaf 2")
                os.system("docker search {0}".format(search_image))
                os.system("tput setaf 6")

            elif docker_choice == 9:
                print("Enter Image Name To Download From Docker HUB : ", end='')
                download_image_name = input()
                print("Enter Version Name of That Image: ", end='')
                download_version_name = input()
                os.system("tput setaf 2")
                os.system("docker pull {0}:{1}".format(
                    download_image_name, download_version_name))
                print("Image Downloaded Successfully.")
                os.system("tput setaf 6")

            elif docker_choice == 10:
                print("Enter Base OS Full Path Were File is Located : ", end='')
                base_os_path1 = input()
                print("Enter Docker Container Image Name: ", end='')
                doc_cont_name1 = input()
                print(
                    "Enter Path Of That Docker Container Were You Would Like To Copy : ", end='')
                path1 = input()
                os.system("tput setaf 2")
                os.system("docker cp {0} {1}:{2}".format(
                    base_os_path1, doc_cont_name1, path1))
                print("Image Copied Successfully To Docker Container.")
                os.system("tput setaf 6")

            elif docker_choice == 11:
                print("Enter Docker Container Image Name: ", end='')
                doc_cont_name2 = input()
                print(
                    "Enter Full Path Of That Docker Container Were File is Located : ", end='')
                path2 = input()
                print(
                    "Enter Path Of Base Os Were You Would Like To Store It  : ", end='')
                base_os_path2 = input()
                os.system("tput setaf 2")
                os.system("docker cp {0}:{1} {2}".format(
                    doc_cont_name2, path2, base_os_path2))
                print("Image Copied Successfully To Base OS.")
                os.system("tput setaf 6")

            elif docker_choice == 12:  # optimize
                print("Enter Docker Container Image Name To Stop It : ", end='')
                stop_doc_cont_name = input()
                os.system("tput setaf 2")
                os.system("docker stop {0}".format(stop_doc_cont_name))
                print("Doker Container Stoped Successfully")
                os.system("tput setaf 6")

            elif docker_choice == 13:  # optimize
                print("""
                        CHOOSE WHAT YOU WOULD LIKE TO DO :
                        PRESS :
                            1. To Remove Particular Image.
                            2. To Remove Particular Image Forcefully.
                            3. To Remove All Images From Docker.
                            4. To Remove All Images From Docker Forcefully.
                            5. Exit From Removing Images.
                """)
                print("Enter Your Choice : ", end='')
                remove_image_choice = int(input())
                if remove_image_choice == 1:
                    print("Enter Docker Image Name To Remove It : ", end='')
                    doc_img_name1 = input()
                    os.system("tput setaf 2")
                    os.system("docker rmi {0}".format(doc_img_name1))
                    print("Doker Image Removed Successfully.")
                    os.system("tput setaf 6")
                elif remove_image_choice == 2:
                    print("Enter Docker Image Name To Remove It Forcefully : ", end='')
                    doc_img_name2 = input()
                    os.system("tput setaf 2")
                    os.system("docker rmi -f {0}".format(doc_img_name2))
                    print("Forcefully Removed Docker Image from Docker.")
                    os.system("tput setaf 6")
                elif remove_image_choice == 3:
                    os.system("tput setaf 2")
                    os.system("docker rmi `docker image ls`")
                    print(
                        "All Docker Image Removed from Docker Accept Those which Are In Use.")
                    os.system("tput setaf 6")
                elif remove_image_choice == 4:
                    os.system("tput setaf 2")
                    os.system("docker rmi -f `docker image ls`")
                    print("All Docker Image Removed Forcefully from Docker.")
                    os.system("tput setaf 6")
                elif remove_image_choice == 5:
                    os.system("tput setaf 3")
                    print(
                        "Ok! We are Exiting You From Remove Dcoker Image Menu to Main Menu.")
                    os.system("tput setaf 6")
                    break
                else:
                    os.system("tput setaf 1")
                    print("Please Choose Valid Option From Menu! Invalid Choice!")
                    os.system("tput setaf 6")

            elif docker_choice == 14:  # optimize
                print("""
                        CHOOSE WHAT YOU WOULD LIKE TO DO :
                        PRESS :
                            1. To Remove Particular Docker Container.
                            2. To Remove Particular Docker Container Forcefully.
                            3. To Remove All Docker Container From Docker.
                            4. To Remove All Docker Container From Docker Forcefully.
                            5. Exit From Removing Docker Container.
                """)
                print("Enter Your Choice : ", end='')
                remove_doc_cont_choice = int(input())
                if remove_doc_cont_choice == 1:
                    print("Enter Docker Container Name To Remove It : ", end='')
                    doc_cont_name_rm1 = input()
                    os.system("tput setaf 2")
                    os.system("docker rm {0}".format(doc_cont_name_rm1))
                    print("Docker Container Removed Successfully.")
                    os.system("tput setaf 6")
                elif remove_doc_cont_choice == 2:
                    print(
                        "Enter Docker Container Name To Remove It Forcefully : ", end='')
                    doc_cont_name_rm2 = input()
                    os.system("tput setaf 2")
                    os.system("docker rm -f {0}".format(doc_cont_name_rm2))
                    print("Forcefully Removed Docker Container from Docker.")
                    os.system("tput setaf 6")
                elif remove_doc_cont_choice == 3:
                    os.system("tput setaf 2")
                    os.system("docker rmi `docker ps -a -q`")
                    print(
                        "All Docker Container Removed from Docker Accept Those which Are In Running State.")
                    os.system("tput setaf 6")
                elif remove_doc_cont_choice == 4:
                    os.system("tput setaf 2")
                    os.system("docker rm -f `docker ps -a -q`")
                    print("All Docker Container Removed Forcefully from Docker.")
                    os.system("tput setaf 6")
                elif remove_doc_cont_choice == 5:
                    os.system("tput setaf 3")
                    print(
                        "Ok! We are Exiting You From Remove Dcoker Container Menu to Main Menu.")
                    os.system("tput setaf 6")
                    break
                else:
                    os.system("tput setaf 1")
                    print("Please Choose Valid Option From Menu! Invalid Choice!")
                    os.system("tput setaf 6")

            elif docker_choice == 15:
                break

            else:
                os.system("tput setaf 1")
                print("Please Choose Valid Option From Menu! Invalid Choice! Try Again!")
                os.system("tput setaf 6")

            print("DO YOU WANT TO CONTINUE USING DOCKER SERVICES ?? PRESS y if YES: ")
            docker_inp = input()
            if docker_inp == 'y':
                pass
            else:
                break

    elif option == 4:
        #import os
        os.system("yum install httpd -y")
        os.system("systemctl stop firwalld")
        os.system("setenforce 0")
        os.system("systemctl restart httpd")
        os.system("systemctl status httpd")
        print("""
        -------------------THIS SYSTEM HAS BEEN CONFIGURED AS WEBSERVER , YOU CAN DEPLOY YOUR SITE--------------------------

            """)

    elif option == 5:
        while True:
            #import os
            print("Create Dynamic Partitions")
            print("ATTACH AN TWO OR MORE HD TO YOUR OS")
            print("AFTER ENTERING fdisk,use following sequence : \n 1:n \n 2:p \n3: 1 \n 4: 3 times enter \n 5: wq ")
            os.system("fdisk -l")
            partition_name1 = input("Enter Partition Full Name : ")
            partition_name2 = input("Enter Second partition full name : ")
            os.system("fdisk {}".format(partition_name1))
            os.system("fdisk {}".format(partition_name2))
            os.system("pvcreate {} {}".format(partition_name1, partition_name2))
            vg_name = input("Enter VOLUME GROUP name: ")
            os.system("vgcreate {} {} {}".format(vg_name, partition_name1, partition_name2))
            print("-----volume group has been created-------")
            lv_name = input("Enter Logical Volume : ")
            size = input("Enter size of logical Volume : ")
            os.system(
                "lvcreate --size {} --name {} {}".format(size, lv_name, vg_name))
            print("--------------------Logical volume has been created--------------")
            os.system("mkfs.ext4 /dev/{}/{}".format(vg_name, lv_name))
            os.system("mkdir /Swift")
            os.system("mount /dev/{}/{} /Swift".format(vg_name, lv_name))
            print("""
                        press:
                            1: pvdisplay
                            2: vgdisplay
                            3: lvdisplay
                            4: Exit
                        """)
            while True:
                x = int(input())
                if x == 1:
                    os.system("pvdisplay {} {}".format(
                        partition_name1, partition_name2))
                elif x == 2:
                    os.system("vgdisplay {} {} {}".format(
                        vg_name, partition_name1, partition_name2))
                elif x == 3:
                    os.system("lvdisplay /dev/{}/{}".format(vg_name, lv_name))
                elif x==4:
                    break
                else :
                    print("error")
            print("Do you want to use LVM SERVICES more ? , if yes press y :")
            lvm_inp = input()
            if lvm_inp == 'y':
                pass
            else:
                break
    print("DO YOU WANT TO USE THESE SERVICES MORE? PRESS y if 'YES' ", end='')
    menu = input()
    if menu == 'y':
        pass
    else:
        break

