<?php

// File to store inventory data
const DATA_FILE = "inventory.json";

// Load existing data
function loadData() {
    if (!file_exists(DATA_FILE)) {
        return [];
    }
    return json_decode(file_get_contents(DATA_FILE), true) ?? [];
}

// Save data to JSON file
function saveData($data) {
    file_put_contents(DATA_FILE, json_encode($data, JSON_PRETTY_PRINT));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $data = loadData();

    if (isset($_POST['add'])) {
        $name = trim($_POST["name"]);
        $quantity = trim($_POST["quantity"]);

        if ($name && $quantity) {
            $data[] = ["name" => $name, "quantity" => $quantity];
            saveData($data);
        }
    } elseif (isset($_POST['delete'])) {
        $nameToDelete = trim($_POST["delete"]);
        $data = array_filter($data, fn($item) => $item["name"] !== $nameToDelete);
        saveData(array_values($data));
    }
}

// Load updated inventory
$inventory = loadData();

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inventory System</title>
</head>
<body>

    <h2>Ingredient Inventory</h2>

    <form method="POST">
        <input type="text" name="name" placeholder="Ingredient Name" required>
        <input type="text" name="quantity" placeholder="Quantity" required>
        <button type="submit" name="add">Add Ingredient</button>
    </form>

    <h3>Current Inventory:</h3>
    <ul>
        <?php foreach ($inventory as $item): ?>
            <li>
                <?= htmlspecialchars($item["name"]) ?>: <?= htmlspecialchars($item["quantity"]) ?>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="delete" value="<?= htmlspecialchars($item["name"]) ?>">
                    <button type="submit">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>

</body>
</html>
