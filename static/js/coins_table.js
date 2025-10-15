function CoinsTable({initialCoins}) {
  const [coins, setCoins] = React.useState(initialCoins || []);
  React.useEffect(() => {
    const socket = new WebSocket(`ws://${window.location.host}/ws/coins/`);

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        setCoins(data);
    };

    socket.onerror = (err) => console.error("WebSocket error:", err);

    return () => socket.close();
  }, []);

  return (
  <>
      <table className="table table-hover">
        <thead>
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
          </tr>
        </thead>
        <tbody>
          {coins.map((coin, i) => (
            <tr key={i}>
              <td>{coin.rank}</td>
              <td>
                <img src={coin.image} alt="" className="px-2" width="50" />
                {coin.name}
                <small className="text-muted px-2">{coin.symbol}</small>
              </td>
              <td style={{ color: coin.state === 'raise' ? 'limegreen' : coin.state === 'fall' ? 'red' : 'inherit' }}>
                {coin.price}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}
