import React from 'react';
import { Card, Button, Container, Image } from 'semantic-ui-react'

export const Reviews = ( {reviews} ) => {
    return (
        <Card.Group itemsPerRow={6}>
        {reviews.map(review => {
            return (
                <Card key={review.id} color={review.impression}>
                    <Card.Content>
                        <Image src={process.env.PUBLIC_URL + 'ella.jpeg'}></Image>
                        <Card.Header> {review.clothing_name} </Card.Header>
                        <Card.Description> {review.text} </Card.Description>
                    </Card.Content>
                    <Card.Content extra>
                    {review.stars} Stars
                    </Card.Content>
              </Card>
            );
        })}
    </Card.Group>
    )
}
