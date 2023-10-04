/*
    Copyright (C) 2023 Jean Kieffer

    This file is part of Arb.

    Arb is free software: you can redistribute it and/or modify it under
    the terms of the GNU Lesser General Public License (LGPL) as published
    by the Free Software Foundation; either version 2.1 of the License, or
    (at your option) any later version.  See <http://www.gnu.org/licenses/>.
*/

#include "acb_theta.h"

#define ACB_THETA_G2_JET_NAIVE_THRESHOLD 10000

void acb_theta_g2_sextic(acb_poly_t res, const acb_mat_t tau, slong prec)
{
    slong g = 2;
    slong n2 = 1 << (2 * g);
    slong nb = acb_theta_jet_nb(1, g);
    fmpz_mat_t mat;
    acb_mat_t w;
    acb_ptr z, dth;

    fmpz_mat_init(mat, 2 * g, 2 * g);
    acb_mat_init(w, g, g);
    dth = _acb_vec_init(n2 * nb);
    z = _acb_vec_init(g);

    acb_siegel_reduce(mat, tau, prec);
    acb_siegel_transform(w, mat, tau, prec);

    if (prec < ACB_THETA_G2_JET_NAIVE_THRESHOLD)
    {
        acb_theta_g2_jet_naive_1(dth, w, prec);
        acb_theta_g2_chi6m2(res, dth, prec);
    }
    else
    {
        acb_theta_jet_all(dth, z, w, 1, prec);
        acb_theta_g2_chi6m2(res, dth, prec);
    }

    sp2gz_inv(mat, mat);
    acb_siegel_cocycle(w, mat, w, prec);
    acb_theta_g2_detk_symj(res, w, res, -2, 6, prec);

    fmpz_mat_clear(mat);
    acb_mat_clear(w);
    _acb_vec_clear(dth, n2 * nb);
    _acb_vec_clear(z, g);
}
