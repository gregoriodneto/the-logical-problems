<?php

function report($data)
{
    $filtering_report = [];
    foreach ($data as $key => $value) {
        $product_id = $value["product_id"];
        if (isset($filtering_report[ $product_id ]))
        {
            $filtering_report[$product_id]["total_quantity"] += $value["quantity"];
            $filtering_report[$product_id]["total_revenue"] += $value["quantity"] * $value["price"];
        }
        else
        {
            $filtering_report[$value["product_id"]] = [
                "product_id" => $product_id,
                "product_name" => ucwords(strtolower($value["product_name"])),
                "total_quantity" => $value["quantity"],
                "total_revenue" => $value["quantity"] * $value["price"],
            ];
        }
    }
    return array_values($filtering_report);
}

$file_path = dirname(__FILE__) ."/sales.json";
$file = file_get_contents($file_path);
$json = json_decode($file, true);
$data = report($json);
print_r($data);