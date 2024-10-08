import React from 'react';
import {Link} from "react-router-dom";
import {Button} from "@mui/material";
import {ShopResponse} from "../api/models/response/ShopResponse";
import './ShopCard.css';

const ShopCard: React.FC<ShopResponse> = ({ id, name, description, price, url_images }) => {
    return (
        <Link to={`/shop/${id}`} className="shop-card">
            <div className="shop-content-text">
                <h3 className="shop-title">{name}</h3>
                <p className="shop-description">{description}</p>
            </div>
            <div className="shop-content-img">
                <img src={url_images[0]} alt={name} className="shop-image" />
            </div>
            <div>
                <p className="shop-price">{price} ₽</p>
            </div>
            <div className="shop-content-action">
                <Button variant="contained" color="error" className="shop-order-button">Заказать</Button>
            </div>
        </Link>
    );
};

export default ShopCard;