<?php

function filters($data)
{
    if ($data["status"] === "invalid" || $data["status"] === "deprecated")
    {
        return null;
    }

    if (isset($data["children"]) && is_array($data["children"]))
    {
        $filteredChildren = [];
        foreach ($data["children"] as $child)
        {
            $filteredChild = filters($child);
            if ($filteredChild !== null)
            {
               $filteredChildren[] = $filteredChild; 
            }
        }

        if (!empty($filteredChildren))
        {
            $data["children"] = $filteredChildren;
        }
        else
        {
            unset( $data["children"] );
        }
    }

    return $data;
}

$file_content = file_get_contents("/home/greg/Documentos/Projetos/Sistemas/the-logical-problems/problems/file_recursive_filters/files_recursive.json");
$json = json_decode($file_content, true);
$data = filters($json);
print_r($data);