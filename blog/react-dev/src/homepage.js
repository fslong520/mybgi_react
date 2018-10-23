import React, { Component } from 'react';
import 'hana-ui/hana-style.scss';
import {Menu,MenuItem,Link,Title,Icon} from 'hana-ui';
class Homepage extends Component {
  render() {

    return (
      <div>
        <Title
          icon={
            <Icon type={'hana'}
            style={{
              margin:'-9px 0px 0px -28px',
            }}
            color={'#199ed8'} />}
          iconRight={
            <div style={{
              padding:'0px',
              margin:'-18px 0px 0px 0px',
            }}>
              <Icon type={'menu'} color={'#199ed8'} />
            </div>
          }
        >
          <Menu auto horizonal type="linear" value="Activities">
            <MenuItem value="Activities">明月不归尘</MenuItem>
            <MenuItem value="Games">
              <Link
                id={'githubLink'}
                href={'https://github.com/fslong520'}
                style={{
                  display: 'block',
                }}
                icon={'github'}
              >
                Github
              </Link>
            </MenuItem>
          </Menu>
        </Title>
      </div>

    );
  }
}

export default Homepage;
