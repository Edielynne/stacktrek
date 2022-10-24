
import React, {useState,useEffect} from 'react';
import data from './data/data.json';
import Posts from './components/posts';
import Pagination from './components/pagination';

  
const Products = () => {
    const [posts, setPosts] = useState([]);
    const[currentPage, setCurrentPage]= useState(1);
    const[postsPerPage, setPostsPage]= useState(10);

    useEffect(() => {
        const fetchPosts =  () => {
        const d = data.map( (info) => {
           
            return info
        })
       setPosts(d);
        }
        fetchPosts();
    }, []);
    const indexOfLastPost = currentPage * postsPerPage;
    const indexOfFirstPost = indexOfLastPost - postsPerPage;
    const currentPosts = posts.slice(indexOfFirstPost, indexOfLastPost);
    

    const paginate = (pageNumber) => setCurrentPage(pageNumber);
  return (
  <div>
    <Posts posts={currentPosts}/>
    <Pagination postsPerPage={postsPerPage} totalPosts={posts.length} paginate={paginate}/>

  
    </div>
  );
};
  
export default Products;