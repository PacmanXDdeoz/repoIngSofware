--
-- PostgreSQL database dump
--

\restrict VpSyaFmR8SNjy9qobT8rJLgnA0oRvQbCzA0ka3ccKk7rzA2hC3O18tfuWargUTC

-- Dumped from database version 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.13 (Ubuntu 16.13-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: books; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.books (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    autor character varying(50) NOT NULL,
    public_date date NOT NULL,
    genere character varying(50) NOT NULL,
    pdf_path text NOT NULL,
    status boolean DEFAULT true
);


ALTER TABLE public.books OWNER TO admin;

--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.books_id_seq OWNER TO admin;

--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Name: books_inlist; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.books_inlist (
    id integer NOT NULL,
    book_id integer NOT NULL,
    list_id integer NOT NULL
);


ALTER TABLE public.books_inlist OWNER TO admin;

--
-- Name: books_inlist_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.books_inlist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.books_inlist_id_seq OWNER TO admin;

--
-- Name: books_inlist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.books_inlist_id_seq OWNED BY public.books_inlist.id;


--
-- Name: lists; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.lists (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.lists OWNER TO admin;

--
-- Name: lists_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.lists_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.lists_id_seq OWNER TO admin;

--
-- Name: lists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.lists_id_seq OWNED BY public.lists.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    username character varying(100),
    email character varying(100) NOT NULL,
    status boolean DEFAULT true,
    password text
);


ALTER TABLE public.users OWNER TO admin;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO admin;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Name: books_inlist id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.books_inlist ALTER COLUMN id SET DEFAULT nextval('public.books_inlist_id_seq'::regclass);


--
-- Name: lists id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.lists ALTER COLUMN id SET DEFAULT nextval('public.lists_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.books (id, title, autor, public_date, genere, pdf_path, status) FROM stdin;
1	El que susurra en la oscuridad	H.P. Lovecraft	1931-08-01	Horror	/home/pacmanxddeoz/Escritorio/repoIngSofware/Proyecto/erp_project/static/documents/El_que_susurra_en_la_oscuridad-H._P._Lovecraft.pdf	t
\.


--
-- Data for Name: books_inlist; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.books_inlist (id, book_id, list_id) FROM stdin;
\.


--
-- Data for Name: lists; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.lists (id, name, user_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users (id, name, lastname, username, email, status, password) FROM stdin;
2	admin	example	\N	admin@example.com	t	$2a$06$dHmGWFTuAcsyYYemZYHOueeC8dTHNQmp1mSRqNVOK205D0CyLeChu
4	Emma	de la Crucito	SoyEmmaDobleM	emma@example.com	t	$2a$06$9yh.6ZYHCkPwRNaXaTAzgeXGX/F8VfzDdaAxJsRlr5nWGdz6cLSnm
5	jona	Puto	SoyPutoAtodahonra	jona@example.com	t	$2a$06$wG9T4QBbw3fgPUNIqeiBwORFW2Zoe5Keq3/jWRAK5h/A/SnGC/hNW
\.


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.books_id_seq', 1, true);


--
-- Name: books_inlist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.books_inlist_id_seq', 1, false);


--
-- Name: lists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.lists_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: books_inlist books_inlist_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.books_inlist
    ADD CONSTRAINT books_inlist_pkey PRIMARY KEY (id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: lists lists_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.lists
    ADD CONSTRAINT lists_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: books_inlist books_inlist_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.books_inlist
    ADD CONSTRAINT books_inlist_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Name: books_inlist books_inlist_list_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.books_inlist
    ADD CONSTRAINT books_inlist_list_id_fkey FOREIGN KEY (list_id) REFERENCES public.lists(id);


--
-- Name: lists lists_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.lists
    ADD CONSTRAINT lists_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

\unrestrict VpSyaFmR8SNjy9qobT8rJLgnA0oRvQbCzA0ka3ccKk7rzA2hC3O18tfuWargUTC

