import os
from flask import Flask, flash, request, redirect, url_for,render_template,send_from_directory,send_file
from werkzeug.utils import secure_filename
from extractor import export_to_csv
UPLOAD_FOLDER = r'C:\Users\Priyanshu Gupta\Desktop\Resume Extractor'
ALLOWED_EXTENSIONS = {'docx', 'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
csv_file=None
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(request.files['file'])
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #print(UPLOAD_FOLDER+'\'+file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            #return redirect(url_for('uploaded_file',
                                    #filename=filename))
            filetosend=UPLOAD_FOLDER+"\\"+file.filename
            #filetosend+=file.filename
            #filetosend=file.filename
            #print(filetosend)
            csv_file=export_to_csv(filetosend)
            #print(csv_file)
            #sec_csv_file=secure_filename(csv_file)
            return redirect(url_for('download_file',
                                    path=csv_file))
        #else:
            #return render_template('response.html') 
    return render_template('index.html')

@app.route('/download/<path>',methods=['GET', 'POST'])
def download_file(path):
    if request.method=='POST':
        print(path)
        return send_file(path,as_attachment=True)     # as_attachment=True do not change the format if false changes csv to xls format
    #return render_template('response.html',path=path)
    return render_template('response.html')
if __name__ == "__main__":
    csv_file=None
    app.run(debug=True)