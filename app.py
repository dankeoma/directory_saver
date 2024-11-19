from flask import Flask, request, jsonify, session
import logging
from d_saver import sqlite_save


logging.basicConfig(filename='error.log',level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return '<h3>Hi I am Daniel, welcome to the File listing API. You are required to \
supply the directory path in the request body as such; "filePath": "D:/Desktop/Pictures"</h3>'
  
#FACULTY
#select all Faculties in the school
@app.route('/view_directory_content/', methods=["POST"])
def directory_content():
    try:
        data = request.get_json()
        if 'filePath' in data and isinstance(data['filePath'],str):
            filePath = data['filePath']
            try:
                dat = sqlite_save(f"{filePath}")
             
                return jsonify({"Data": dat,
                                "Status": "Success",
                                "Code": "00",
                                "Message": "File list generated successfully"})
            except Exception:
                app.logger.error("Error: The provided document PATH does not exist")
                return jsonify({"Data": None,
                                "Status": "Failed",
                                "Code": "01",
                                "Message": "Error: The provided document PATH does not exist"})
        else:
            app.logger.error("Error: filePath either missing from the request body or is not of string type")
            return jsonify({"Data": None,
                                "Status": "Failed",
                                "Code": "01",
                                "Message": "Error: filePath either missing from the request body or is not of string type"})
    except Exception:
        app.logger.error("Error: something went wrong, make sure request body exixts")
        return jsonify({"Data": None,
                                "Status": "Failed",
                                "Code": "01",
                                "Message": "Error: something went wrong, make sure request body exixts"})
        
if __name__ == '__main__':
    app.run(debug=True)
