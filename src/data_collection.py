import csv

# Mock data to simulate API response
mock_data = [
    {'id': '1', 'link': 'https://example.com/pin1', 'note': 'Fashion trend 1', 'image': {'original': {'url': 'https://example.com/image1.jpg'}}, 'created_at': '2024-07-28'},
    {'id': '2', 'link': 'https://example.com/pin2', 'note': 'Fashion trend 2', 'image': {'original': {'url': 'https://example.com/image2.jpg'}}, 'created_at': '2024-07-28'},
    {'id': '3', 'link': 'https://example.com/pin3', 'note': 'Fashion trend 3', 'image': {'original': {'url': 'https://example.com/image3.jpg'}}, 'created_at': '2024-07-28'}
]

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Link', 'Note', 'Image URL', 'Created At'])
        for row in data:
            writer.writerow([row['id'], row['link'], row['note'], row['image']['original']['url'], row['created_at']])

if __name__ == "__main__":
    save_to_csv(mock_data, 'mock_pinterest_pins.csv')
    print(f"Saved {len(mock_data)} pins to mock_pinterest_pins.csv")
