import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Typography } from '@material-ui/core';

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
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  fullWidth: {
    width: '100%',
  },
  image: {
    paddingTop: "0px",
    paddingLeft: "295px",
    alignContent: "center",
  },
}));

function MainContent() {
  const classes = useStyles()
  return (
    <main className={classes.fullWidth}>
      <div className={classes.toolbar} />
      <img className ={classes.image} src={process.env.PUBLIC_URL + 'ella.jpeg'}/>
      <div className={classes.content}>
        <Typography paragraph>
          Welcome to Ella App, Your closet simplified. Please upload pictures of your clothing items.
        </Typography>
      </div>
    </main>
  );
}

export default MainContent;