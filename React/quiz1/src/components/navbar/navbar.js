import React from 'react';
import{
    Nav,
    NavLink,
    Bars,
    NavMenu,
    NavBtn,
    NavBtnLink,
} from './NavbarElements';
import { BiSearchAlt } from "react-icons/bi";
const Navbar = () => {
    return (
        <>
      <Nav>
        <Bars />
  
        <NavMenu>
          <NavLink to='/about' activeStyle>
            About
          </NavLink>
        
        
          <NavLink to='/team' activeStyle>
        
            Teams
          </NavLink>
          
          <NavLink to='/blogs' activeStyle>
            Blogs
          </NavLink>
          <NavLink to='/sign-up' activeStyle>
            Sign up
          </NavLink>
          <form className = "search">
      <input type="text" placeholder="Search.." name="search"></input>
      <button type="submit"><BiSearchAlt/></button>
    </form>

          {/* Second Nav */}
          {/* <NavBtnLink to='/sign-in'>Sign In</NavBtnLink> */}
        </NavMenu>
       
        <NavBtn>
          <NavBtnLink to='/signin'>Log in</NavBtnLink>
        </NavBtn>
      </Nav>
    </>
    )
}
 export default Navbar;
