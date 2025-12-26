import { useEffect, useState } from "react";
import { poemAPI } from "./services/api";
import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";

function App() {
  const [poems, setPoems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadPoems = async () => {
    try {
      setLoading(true);
      const data = await poemAPI.getAllPoems();
      console.log("Получены стихи:", data);
      setPoems(data);
      setError("");
    } catch (error) {
      console.error("Ошибка:", error);
      setError("Не удалось загрузить стихи");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadPoems();
  }, []);

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="spinner">
          <p>Поэзия грузится, чуть-чуть терпения ...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="app">
      <Header />

      <main className="main-content">
        <div className="content-wrapper">
          <div className="poems-container">
            <div className="stats">
              <p>Всего стихов: {poems.length}</p>
            </div>

            {/* start poem-list */}
            <div className="poems-list">
              {poems.map((poem) => (
                <div className="poem-card" key={poem.id}>
                  <h2 className="poem-title">{poem.title}</h2>
                  <div className="poem-author">
                    Автор:{" "}
                    {poem.author.pseudonym
                      ? poem.author.pseudonym
                      : poem.author.username}
                  </div>
                  <div className="poem-body">
                    {poem.body.split("\r\n").map((line, index) => (
                      <p key={index} className="poem-line">
                        {line || <br />}
                      </p>
                    ))}
                  </div>

                  <div className="poem-meta">
                    <span className="poem-date">
                      Дата:{" "}
                      {new Date(poem.created_at).toLocaleDateString("ru-Ru")}
                    </span>
                    <br />
                    <span>
                      Время:{" "}
                      {new Date(poem.created_at).toLocaleTimeString("ru-Ru")}
                    </span>
                  </div>
                </div>
              ))}
            </div>
            {/* end poem-list */}
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
}

export default App;
