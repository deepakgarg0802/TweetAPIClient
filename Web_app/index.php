<!DOCTYPE html>
<html>
<?php
	$result= exec('/usr/bin/python2.7 ./scripts/fetch_tweets.py', $out);
	//Load the json file retrieved from python script
?>
<head>
	<title>Filtered Tweets</title>
	<style type="text/css">
		body{
		}
	    .tweet{
        border-radius: 4px 4px 4px 4px;
		-moz-border-radius: 4px 4px 4px 4px;
		-webkit-border-radius: 4px 4px 4px 4px;
		border: 0px solid #000000;
        -webkit-box-shadow: 8px 8px 8px -5px rgba(0,0,0,0.75);
		-moz-box-shadow: 8px 8px 8px -5px rgba(0,0,0,0.75);
		box-shadow: 8px 8px 8px -5px rgba(0,0,0,0.75);
		background-color: #d9edf7;
		margin-top: 8px;
		margin-bottom: 8px;
      }
      p{
      	text-align: right;
      }
    </style>
</head>

<body>
	<div class="container-fluid">
		<div class="container">
			<h1>Popular Tweets with #custserv</h1>
		</div>

		<div class="container">
			
			<?php
				foreach($out as $key => $value) 
				{
				    $values = json_decode($value, true);
				    
				    foreach($values as $index => $element) // $index contains Screen_name and $element contains the tweet text
				    {
				        echo "<div class=\"container tweet\">"."<h3>".$index."</h3>"."<p>".$element."<br></div>";
				    }
				}
			?>	
					
		</div>
	</div>          

</body>
</html>
