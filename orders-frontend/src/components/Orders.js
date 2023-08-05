import { useEffect, useState } from "react";

export const Orders = () => {
    const [id, setId] = useState('');
    const [quantity, setQuantity] = useState('');
    const [isQuantityEntered, setIsQuantityEntered] = useState(false);
    const [message, setMessage] = useState('Buy your favorite product');

    useEffect(() => {
        if (isQuantityEntered) {
            (async () => {
                try {
                    const response = await fetch(`http://inv-app-service/products/${id}`);
                    const content = await response.json();
                    const price = parseFloat(content.price) * 1.2;
                    setMessage(`Your product price is $${price * quantity}`);
                } catch (e) {
                    setMessage('Buy your favorite product');
                }
            })();
        }
    }, [id, quantity, isQuantityEntered]);

    const submit = async e => {
        e.preventDefault();

        await fetch('http://pay-app-service/orders', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                id,
                quantity
            })
        });

        setMessage('Thank you for your order!');
    }

    const handleQuantityChange = e => {
        setQuantity(e.target.value);
        setIsQuantityEntered(true);
    }

    return (
        <div className="container">
            <main>
                <div className="py-5 text-center">
                    <h2>Checkout form</h2>
                    <p className="lead">{message}</p>
                </div>

                <form onSubmit={submit}>
                    <div className="row g-3">
                        <div className="col-sm-6">
                            <label className="form-label">Product</label>
                            <input className="form-control" onChange={e => setId(e.target.value)} />
                        </div>

                        <div className="col-sm-6">
                            <label className="form-label">Quantity</label>
                            <input type="number" className="form-control" onChange={handleQuantityChange} />
                        </div>
                    </div>
                    <hr className="my-4" />
                    <button className="w-100 btn btn-primary btn-lg" type="submit">Buy</button>
                </form>
            </main>
        </div>
    );
}
