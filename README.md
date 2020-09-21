<html>
<body>
<?php
$html = file_get_contents('https://livecounts.io/tiktok-realtime/saxon.nottz');

$doc1 = new DOMDocument();

libxml_use_internal_errors(TRUE); //disable libxml errors

if(!empty($html)){ //if any html is actually returned

        $doc1->loadHTML($html);
        libxml_clear_errors(); //remove errors for yucky html
        $xmen = new DOMXPath($doc1);

        //get all the h2's with an id
        $xmen_11 = $xmen->query('//body');
        $i=0;
        if($xmen_11->length > -1){
                 foreach($xmen_11 as $row){
                        $values = $row->nodeValue;
                        preg_match_all('!\d+!', $values, $matches);
                        var_dump($matches);
                        $i++;
                }
        }
}
?>
</body>
</html>

