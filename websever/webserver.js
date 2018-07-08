var http = require('http');
var fs = require('fs');
var formidable = require('formidable');
var cmd = require('node-cmd');

// html file containing upload form
var upload_html = fs.readFileSync("upload_file.html");
var playing_html = fs.readFileSync("playing.html");

// replace this with the location to save uploaded files
var upload_path = "/home/pi/red/websever/music/";

console.log('Starting server...')

http.createServer(function (req, res) {
    if (req.url == '/uploadform') {
        console.log('got contection to uploadform');
        res.writeHead(200);
        res.write(upload_html);
        return res.end();
    } else if (req.url == '/fileupload') {
        console.log('got conection to fileupload');
        res.writeHead(200);
        res.write(playing_html);
        res.end();
        console.log('delt static content to client');
        console.log('attempting formiable parse');
        var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            // oldpath : temporary folder to which file is saved to
            console.log('parse sucess!');
            var oldpath = files.filetoupload.path;
            var newpath = upload_path + files.filetoupload.name.replace(/\s/g, '');
            console.log('validating file before saving');
            if (newpath.slice(-4) != '.mp3') {
                //Change the file name to something the computer gets
                newpath += '.mp3';
            };
            //Change the file name to something the computer gets
            // copy the file to a new location
            fs.rename(oldpath, newpath, function (err) {
                console.log('moved file');
                if (err) throw err;
                // you may respond with another html page
                newpath = '/"' + newpath + '/"';
                var command = 'sudo python ../../lightshowpi/py/synchronized_lights.py --file=' + newpath;
                console.log('atempting to call lightshow NOW!');
                cmd.run(command);
            });
        });
    }
}).listen(1337);

console.log('Non-fatal Sucess! server proballly up!');
