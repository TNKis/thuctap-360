async function fetchUser(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    if (!response.ok) throw new Error('Network error');
    
    const user = await response.json();
    console.log('User:', user);
  } catch (error) {
    console.error('Lỗi khi gọi API:', error);
  }
}

// Gọi hàm để fetch user có id = 1
fetchUser(1);
