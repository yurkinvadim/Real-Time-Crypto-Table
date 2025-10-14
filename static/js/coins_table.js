function CoinsTable() {
  const [coins, setCoins] = React.useState([]);      // <-- React.useState
  React.useEffect(() => {                             // <-- React.useEffect
    const socket = new WebSocket("ws://127.0.0.1:8000/ws/coins/");

    socket.onopen = () => {
      console.log("Connected to Coins WebSocket");
    };

    socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        setCoins((prev) => [...prev, data]);
      } catch (err) {
        console.error("Invalid JSON:", event.data);
      }
    };

    socket.onclose = () => console.log("Coins WebSocket closed");
    socket.onerror = (err) => console.error("WebSocket error:", err);

    return () => socket.close();
  }, []);

  return (
    <div>
      <h3>Coins Data</h3>
      <ul>
        {coins.map((c, i) => (
          <li key={i}>{JSON.stringify(c)}</li>
        ))}
      </ul>
    </div>
  );
}
