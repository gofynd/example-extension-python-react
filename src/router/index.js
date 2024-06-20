import { createBrowserRouter } from "react-router-dom";
import { routeGuard } from "./guard";

import Home from "../views/Home";

const router = createBrowserRouter([
  {
    path: "/company/:company_id/",
    element: <Home />,
    loader: routeGuard,
  },
  {
    path: "/company/:company_id/application/:application_id",
    element: <Home />,
    loader: routeGuard,
  },
]);

export default router;
