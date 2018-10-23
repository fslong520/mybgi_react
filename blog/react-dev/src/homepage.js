import React, { Component } from 'react';
import 'hana-ui/hana-style.scss';
import {Title,Icon} from 'hana-ui';
class Homepage extends Component {
  render() {
    return (
      <div>
        <Title
          style={{
            padding: 10,
            backgroundColor: '#19ded8',
            color: 'white',
          }}
        >
          <a href="/">明月不归尘</a>
          <a href="https://github.com/fslong520">
            <Icon type={'github'} color={'#070f66'} />
            github
          </a>

        </Title>

      </div>
    );
  }
}

export default Homepage;
