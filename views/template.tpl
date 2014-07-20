<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Prayer times</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

    <!-- Optional theme -->
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

    <!-- Latest compiled and minified JavaScript -->
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
  </head>


<body>
  <div class="container">
    <h1>Prayer times for {{city}}</h1>

    <p><b>Date: </b>{{date}}</p>

    <table class="table table-hover">
      <tr>
        <th>Fajr</th>
        <th>Shuruk</th>
        <th>Dhuhr</th>
        <th>Assr</th>
        <th>Magreb</th>
        <th>Ishaa</th>
      </tr>

      <tr>
        <td>{{today[4]}}</td>
        <td>{{today[5]}}</td>
        <td>{{today[6]}}</td>
        <td>{{today[7]}}</td>
        <td>{{today[8]}}</td>
        <td>{{today[9]}}</td>
      </tr>
    </table>
  </div>
</body>

</html>
