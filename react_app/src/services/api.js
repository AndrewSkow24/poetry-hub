const API_URL = "http://127.0.0.1:8000/api";

export const poemAPI = {
  // метод получения всех произведений
  getAllPoems: async () => {
    const response = await fetch(`${API_URL}/poem/`);
    if (!response.ok) {
      throw new Error("Ошибка загрузки стихов");
    }
    return response.json();
  },
};
