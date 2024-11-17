
def sqlite_save(directory):
    import sqlite3
    import os
    import datetime
    #A function that lists all the files in a directory
    def filepaths(path):
        file_paths = []
        entries = os.listdir(path)
        for entry in entries:
            entry_with_path = os.path.join(path, entry)
            if os.path.isdir(entry_with_path):
                continue
            else:
                file_paths.append(entry_with_path) 
                
        return file_paths
    
    
    try:
        if os.path.realpath('document.db'):
            os.remove('document.db')
         
        #Create a databse and establish a connection
        mydb = sqlite3.connect('file:document.db?mode=rwc',uri=True)
        my_cursor = mydb.cursor()
        
        #Get the Directory name
        dr_name = directory.split('/')[-1]
        
        #create table bearing the directory nam
        sql = 'create table {} (id integer primary key autoincrement, fileName varchar(100),  fileSize integer, fileType varchar(100), dateCreated datetime )'.format(dr_name)
        my_cursor.execute(sql)
        mydb.commit()
        
        #Loop through the directory and insert the files into database
        for file in filepaths(directory):
            filepart = os.path.splitext(file)[0]
            filename = filepart.split('\\')[-1]
            filetype = os.path.splitext(file)[1]
            filesize = os.path.getsize(file)
            # filedate = time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(time.ctime(os.path.getctime(file))))
            filedate = datetime.datetime.fromtimestamp(os.path.getctime(file))
            
            sql = 'insert into {} (fileName,fileSize,fileType,dateCreated) values(?,?,?,?)'.format(dr_name)
            my_cursor.execute(sql,(filename,filesize,filetype,filedate))
            mydb.commit()
            
            # print(filename)
            
        sql = 'select * from {} '.format(dr_name)
        my_cursor.execute(sql)
        dat = my_cursor.fetchall()
        print(dat)
    except Exception:
        print ("Database already exists!!!")
        
    
sqlite_save("C:/Users/hp/Pictures")



