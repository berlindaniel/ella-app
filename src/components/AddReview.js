import React, { useState, useEffect, Component } from 'react';
import './FormContent.css';
import { makeStyles } from '@material-ui/core/styles';
import { Typography } from '@material-ui/core';
import {Form, Rating, Input, Header, Button, Dropdown } from 'semantic-ui-react';
import { useHistory, withRouter, BrowserRouter } from 'react-router-dom';

var angryEmoji = String.fromCodePoint(0x1F621);
var confidentEmoji = String.fromCodePoint(0x1F920);
var complimentEmjoi = String.fromCodePoint(0x1F601);
var pensiveEmjoi = String.fromCodePoint(0x1F914);

const useStyles = makeStyles(theme => ({
    toolbar: theme.mixins.toolbar,
    title: {
      flexGrow: 1,
      backgroundColor: theme.palette.background.default,
      padding: theme.spacing(3),
      fontSize: 30,
      textAlign: "center",
    },
    content: {
      textAlign: "center",
      flexGrow: 1,
      padding: theme.spacing(3),
    },
    fullWidth: {
      width: '100%',
    },
    labels: {
      alignContent: "center",
      textAlign: "center",
      marginLeft: 10,
      marginBottom: 10,
      display: 'block',
    },
    inputs: {
      margin: "auto",
      //width: "50%",
      alignContent: "center",
      textAlign: "center",
      //marginLeft: 150,
      marginBottom: 10,
      display: 'block',
    },
    cancelbtn:{
      fontSize: 20,
      marginLeft: 300,
      marginRight: 20,

    },
    signupbtn:{
      fontSize: 20,
      marginLeft: 50,
      //marginRight: 20,

    },
    image: {
      paddingTop: "0px",
      paddingLeft: "295px",
      alignContent: "center",
    },
  }));
const impressionOptions = [
    {
      key: 'Confidnece',
      text: 'This outfit makes me feel confident ' + confidentEmoji,
      value: 'blue',
    },
    {
      key: 'Red',
      text: 'Someone else has this outfit ' + angryEmoji,
      value: 'red',
    },
    {
      key: 'Yellow',
      text: 'I got complimented on this outfit ' + complimentEmjoi,
      value: 'yellow',

    },
    {
      key: 'Green',
      text: 'I want to remember this outfit ' + pensiveEmjoi,
      value: 'green',

    },
];
const occasionOptions = [
    {
      key: 'Athletic',
      text: 'Athletic',
      value: 'Athletic',
    },
    {
      key: 'Casual',
      text: 'Casual',
      value: 'Casual',
    },
    {
      key: 'Formal',
      text: 'Formal',
      value: 'Formal',
    },
    {
      key: 'Cold',
      text: 'Cold',
      value: 'Cold',
    },
    {
      key: 'Cozy',
      text: 'Cozy',
      value: 'Cozy',
    },
    {
      key: 'Stylish',
      text: 'Stylish',
      value: 'Stylish',
    },
];

function AddReview({clothes, onNewReview}) {
  const classes = useStyles();
  const [clothing_id, setClothingId] = useState("");
  const [impression, setImpression] = useState("");
  const [rating, setStars] = useState(3);
  const [text, setText] = useState("");
  const [error, setError] = useState("");
  const clothingOptions = clothes.map(clothing =>
    {
      return(
        {
          "key" : clothing.id,
          "value" : clothing.id,
          "text" : clothing.name
        })
    });

  let history = useHistory();

  const redirectToHome = () => {
    history.push("/")
  }

  return (
      <main className={classes.fullWidth}>
          <div className={classes.toolbar} />
          <div className={classes.content}>
              <h2> Review a clothing item </h2>
              <Form>
                  <Form.Field>
                      <Dropdown
                          placeholder='Select Clothing Item to Review'
                          fluid
                          search
                          selection
                          value={clothing_id}
                          options={clothingOptions}
                          onChange={(e,data) => setClothingId(data.value)}
                      />
                  </Form.Field>
                  <Form.Field>
                      <Dropdown
                          placeholder='Clothing Impression'
                          fluid
                          selection
                          options={impressionOptions}
                          onChange={(e,data) => setImpression(data.value)}
                          value={impression}
                      />
                  </Form.Field>
                  <Form.Field>
                      <Input
                          placeholder="Write a review of this clothing item"
                          value={text}
                          onChange={(e,data) => setText(data.value)}
                      ></Input>
                  </Form.Field>
                  <Form.Field>
                    <Rating icon='star' defaultRating={3} maxRating={5}
                      value={rating}
                      onRate={(e, {rating}) => {e.preventDefault(); setStars(rating)}}
                      size='huge'/>
                  </Form.Field>

                  <Button primary onClick={async() => {
                      const review = {clothing_id, impression, rating, text};
                      const response = await fetch("/review", {
                          method: 'POST',
                          headers: {
                              'Content-type': 'application/json'
                          },
                          body: JSON.stringify(review)
                      });
                      if (response.ok) {
                          console.log('success');
                          onNewReview(review);
                          setError("");
                          setStars(3);
                          setClothingId("");
                          setText("");
                          setImpression("");
                      }
                      else {
                          setError("Invalid review, please try again!");
                      }
              }}> Submit </Button>
          { {error} && <Header as='h4' color='red'> {error} </Header> }
          <Button secondary className={classes.centered} onClick={async() => {
          redirectToHome();
          }}>
            Generate More Outfits
          </Button>
          </Form>
      </div>
  </main>
  );
}

  export default AddReview;
