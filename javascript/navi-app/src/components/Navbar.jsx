import React, { Component } from 'react'
import {Link} from 'react-router-dom';
export default class Navbar extends Component {
  render() {
    return (
      <React.Fragment>
        <nav className='navbar navbar-expand-sm bg-primary '>
            <div className="container">
                <ul className='navbar-nav '>
                    <li className='nav-item'>
                        <Link to='/' className='nav-link navbar-brand text-white'>Home</Link>
                    </li>
                    <li className='nav-item '>
                        <Link to='/register' className='nav-link navbar-brand text-white'>Register</Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/login' className='nav-link navbar-brand text-white'>Login</Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/about' className='nav-link navbar-brand text-white'>About</Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/contact' className='nav-link navbar-brand text-white'>Contact</Link>
                    </li>
                </ul>
            </div>
        </nav>
      </React.Fragment>
    )
  }
}
