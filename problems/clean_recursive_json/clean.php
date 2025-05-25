<?php
// Requisição: https://coderbyte.com/api/challenges/json/json-cleaning
// Remover recursivamente "N/A", "", "-"
function clean($data)
{
    foreach ($data as $key => $value) {
        if (is_array($value)) 
        {
            $data[$key] = clean($value);
            if (empty($data[$key]))
            {
                unset($data[$key]);
            }
        }
        elseif ($value === "N/A" || $value === "-" || $value === "")
        {
            unset($data[$key]);
        }
    }
    return $data;
}

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,"https://coderbyte.com/api/challenges/json/json-cleaning");
curl_setopt($ch, CURLOPT_RETURNTRANSFER,true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION,true);

$response = curl_exec($ch);
curl_close( $ch );

if (!$response)
{
    echo "Erro ao fazer requisição";
    exit;
}

$data = json_decode($response, true);
if (json_last_error() !== JSON_ERROR_NONE)
{
    echo "Erro ao decodificar o JSON: " . json_last_error_msg();
    exit;
}

$clean_data = clean($data);

header('Content-Type: application/json');
echo json_encode($clean_data);