const form = document.getElementById('vqaForm');
const responseDiv = document.getElementById('response');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const imageInput = document.getElementById('image');
  const questionInput = document.getElementById('question');

  if (imageInput.files.length === 0) {
    alert('Selecione uma imagem!');
    return;
  }

  const formData = new FormData();
  formData.append('image', imageInput.files[0]);
  formData.append('question', questionInput.value);

  try {
    // Adjust the URL for the backend container (localhost:3000)
    const res = await fetch('http://localhost:3000/vqa', {
      method: 'POST',
      body: formData
    });

    if (!res.ok) {
      throw new Error('Error in the request to the backend');
    }

    const data = await res.json();
    responseDiv.textContent = `Answer: ${data.answer}`;
  } catch (err) {
    console.error(err);
    responseDiv.textContent = 'Error processing the request.';
  }
});

