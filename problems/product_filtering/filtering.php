<?php

function filtering($data)
{
    $filtering_data = [];
    foreach ($data as $key => $value) 
    {        
        if ($value["status"] === "active" && $value["stock"] > 0)
        {                  
            if ($value["price"] === null || $value["price"] === 0)
            {
                $value["price"] = 9.99;
            }
            else
            {
                $value["price"] = (float) $value["price"];
            }
            $value["name"] = ucfirst(strtolower($value["name"]));
            $filtering_data[$key] = $value;
        }
    }
    return $filtering_data;
}

$file_path = dirname(__FILE__) ."/products.json";
$file = file_get_contents($file_path);
$data = json_decode($file, true);
$result = filtering($data);
print_r($result);